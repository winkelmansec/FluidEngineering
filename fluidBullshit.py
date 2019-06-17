import math

class WarmerFluidProperties:
    def __init__(self, m_w, p, k_f, v, capT1, alpha, capPR):
        self.m_w = m_w
        self.p = p
        self.k_f = k_f
        self.v = v
        self.capT1 = capT1
        self.alpha = alpha
        self.capPR = capPR


class ColderFluidProperties:
    def __init__(self, m_c, p, k_f, v, capt1, alpha, capPR):
        self.m_c = m_c
        self.p = p
        self.k_f = k_f
        self.v = v
        self.capt1 = capt1
        self.alpha = alpha
        self.capPR = capPR


#C Shell Data
class TubingSizes:
    def __init__(self, capID_t, capN_t, capOD_t, capN_p):
        self.capID_t = capID_t
        self.capN_t = capN_t
        self.capOD_t = capOD_t
        self.capN_p = capN_p


class ShellData:
    def __init__(self, capD_S, capB, capN_b, capP_t, c):
        self.capD_S = capD_S
        self.capB = capB
        self.capN_b = capN_b
        self.capP_t = capP_t
        self.c = c

def warmer_fluid_input():
    warmerProperties.m_w = float(input("warm m_w: "))
    warmerProperties.p = float(input("warm p: "))
    warmerProperties.k_f = float(input("warm k_f: "))
    warmerProperties.v = float(input("warm v: "))
    warmerProperties.capT1 = float(input("warm capT1: "))
    warmerProperties.alpha = float(input("warm alpha: "))
    warmerProperties.capPR = float(input("warm capPR: "))

    return warmerProperties.m_w, warmerProperties.p, warmerProperties.k_f, warmerProperties.v, warmerProperties.alpha, warmerProperties.capPR

def cooler_fluid_input():
    ColderFluidProperties.m_c = float(input("cold m_c: "))
    ColderFluidProperties.p = float(input("cold p: "))
    ColderFluidProperties.k_f = float(input("cold k_f: "))
    ColderFluidProperties.v = float(input("cold v: "))
    ColderFluidProperties.capt1 = float(input("cold capt1: "))
    ColderFluidProperties.alpha = float(input("cold alpha: "))
    ColderFluidProperties.capPR = float(input("cold capPR: "))

    return ColderFluidProperties.m_c, ColderFluidProperties.p, ColderFluidProperties.k_f, ColderFluidProperties.v, ColderFluidProperties.alpha, ColderFluidProperties.capPR


def tubing_sizes_input():
    TubingSizes.capID_t = float(input("capID_t: "))
    TubingSizes.capN_t = float(input("capN_t: "))
    TubingSizes.capOD_t = float(input("capOD_t: "))
    TubingSizes.capN_p = int(input("capN_p: "))

    return TubingSizes.capID_t, TubingSizes.capN_t, TubingSizes.capOD_t, TubingSizes.capN_p


def shell_input():
    ShellData.capD_S = float(input("capD_S: "))
    ShellData.capB = float(input("capB: "))
    ShellData.capN_b = int(input("capN_b: "))
    ShellData.capP_t = float(input("capP_t: "))
    ShellData.c = float(ShellData.capP_t) - float(TubingSizes.capOD_t)

    return ShellData.capD_S, ShellData.capB, ShellData.capN_b, ShellData.capP_t, ShellData.c


warmerProperties = WarmerFluidProperties(0, 0, 0, 0, 0, 0, 0)
colderProperties = ColderFluidProperties(0, 0, 0, 0, 0, 0, 0)
tubingProperties = TubingSizes(0, 0, 0, 0)
shellProperties = ShellData(0, 0, 0, 0, 0)

# warmer_fluid_input()
# cooler_fluid_input()
# tubing_sizes_input()
# shell_input()

# print("m_w: " + str(warmerProperties.m_w))
# print("m_c: " + str(ColderFluidProperties.m_c))
# print("Shell Properties C: " + str(ShellData.c)

#D Flow Area's

def FlowAreasTube():
    capA_t = ((float(TubingSizes.capN_t) * math.pi) * (math.pow(TubingSizes.capID_t, 2)))/(4 * TubingSizes.capN_p)
    print(capA_t)

def FlowAreasShell():
    capA_s = (ShellData.capD_S * ShellData.c * float(ShellData.capB)) / ShellData.capP_t
    print(capA_s)

# FlowAreasTube()
# FlowAreasShell()

#E Fluid Velocities
