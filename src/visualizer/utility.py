from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from .positions import orange, green, purple, brown, yellow
import numpy as np

def cuboid_data2(o, size=(1,1,1)):
    X = [[[0, 1, 0], [0, 0, 0], [1, 0, 0], [1, 1, 0]],
         [[0, 0, 0], [0, 0, 1], [1, 0, 1], [1, 0, 0]],
         [[1, 0, 1], [1, 0, 0], [1, 1, 0], [1, 1, 1]],
         [[0, 0, 1], [0, 0, 0], [0, 1, 0], [0, 1, 1]],
         [[0, 1, 0], [0, 1, 1], [1, 1, 1], [1, 1, 0]],
         [[0, 1, 1], [0, 0, 1], [1, 0, 1], [1, 1, 1]]]
    X = np.array(X).astype(float)
    for i in range(3):
        X[:,:,i] *= size[i]
    X += np.array(o)
    return X

def plotCubeAt2(positions,sizes=None,colors=None, **kwargs):
    if not isinstance(colors,(list,np.ndarray)): colors=["C0"]*len(positions)
    if not isinstance(sizes,(list,np.ndarray)): sizes=[(1,1,1)]*len(positions)
    g = []
    for p,s,c in zip(positions,sizes,colors):
        g.append( cuboid_data2(p, size=s) )
    return Poly3DCollection(np.concatenate(g),  
                            facecolors=np.repeat(colors,6), **kwargs)
  
def get_collection(structures, thickness):
    position = []
    sizes = []
    colors = []
    max_l = 0.0
    max_w = 0.0
    max_h = 0.0
    for structure in structures:
        if str(type(structure)) != "<class 'skmd.network.Network'>":
            try:
                max_l = max(max_l, structure.l)
                max_w = max(max_w, 5 * structure.w)
            except:
                try:
                    max_l = max(max_l, structure.d)
                except:
                    try:
                        max_l = max(max_l, structure.l1 + structure.l2 + structure.w0)
                        max_w = max(max_w, 1.2 * 2 * (structure.l0 + structure.w))
                    except:
                        pass
            
            max_h = max(max_h, structure.h)

    x_lim = (1.1*1000*max_w)/2.0
    y_lim = 0.0
    z_lim = 0.0
    y = 0.0
    z = 0.0
    for structure in structures:
        z = 0.0
        if str(type(structure)) == "<class 'skmd.structure.Microstripline'>":
            # ground
            position.append((-1000*max_w/2.0,y,z))
            z = z + thickness*1e-3
            sizes.append((1000*max_w,1000*structure.l,thickness*1e-3))
            colors.append(brown)
            # substrate
            position.append((-1000*max_w/2.0,y,z))
            z = z + 1000*max_h
            sizes.append((1000*max_w,1000*structure.l,1000*max_h))
            colors.append(orange)
            # strip
            position.append((-1000*structure.w/2.0,y,z))
            z = z + thickness*1e-3
            sizes.append((1000*structure.w,1000*structure.l,thickness*1e-3))
            colors.append(yellow)

            y = y + 1000*structure.l

        elif str(type(structure)) == "<class 'skmd.structure.MSL_gap'>":
            # ground
            position.append((-1000*max_w/2.0,y,z))
            z = z + thickness*1e-3
            sizes.append((1000*max_w,1000*structure.d,thickness*1e-3))
            colors.append(brown)
            # substrate
            position.append((-1000*max_w/2.0,y,z))
            z = z + 1000*max_h
            sizes.append((1000*max_w,1000*structure.d,1000*max_h))
            colors.append(green)

            y = y + 1000*structure.d
        
        elif str(type(structure)) == "<class 'visualizer.network.Stub'>":
            #ground
            position.append((-1000*max_w/2.0,y,z))
            z = z + thickness*1e-3
            sizes.append((1000*max_w,1000*(structure.l1 + structure.l2 + structure.w0),thickness*1e-3))
            colors.append(brown)
            # substrate
            position.append((-1000*max_w/2.0,y,z))
            z = z + 1000*max_h
            sizes.append((1000*max_w,1000*(structure.l1 + structure.l2 + structure.w0),1000*max_h))
            colors.append(orange)
            #stub
            position.append((-1000*structure.w/2.0,y,z))
            z = z + thickness*1e-3
            sizes.append((1000*structure.w, 1000*(structure.l1 + structure.l2 + structure.w0), thickness*1e-3))
            colors.append(yellow)
            position.append((1000*structure.w/2.0, y + 1000*structure.l1, z))
            sizes.append((1000*structure.l0, 1000*structure.w0, thickness*1e-3))
            colors.append(yellow)

            y = y + 1000*(structure.l1 + structure.l2 + structure.w0)

        elif str(type(structure)) == "<class 'skmd.network.Network'>":
            # ground
            position.append((-1000*max_w/2.0,y,z))
            z = z + thickness*1e-3
            sizes.append((1000*max_w,1000*max_l,thickness*1e-3))
            colors.append(brown)
            # network
            position.append((-1000*max_w/2.0,y,z))
            z = z + 1000*max_h
            sizes.append((1000*max_w,1000*max_l,1000*max_h))
            colors.append(purple)

            y = y + 1000*max_l
        
        y_lim = max(y_lim, 1.1*y)
        z_lim = max(z_lim, 1.1*z)
        
    return [x_lim, y_lim, z_lim, plotCubeAt2(positions=position, sizes=sizes, colors=colors, edgecolor="k")]
            
            

