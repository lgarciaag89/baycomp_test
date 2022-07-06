import baycomp as bc
import numpy as np
import matplotlib.pyplot as plt

import data
from data import get_data



if __name__ == '__main__':
    T1T5_500 = np.array([0.75336, 0.79385, 0.64004, 0.62851, 0.75019, 0.80813, 0.74433, 0.80335])
    T1T5_1500 = np.array([0.79073, 0.76489, 0.66309, 0.64565, 0.74482, 0.79619, 0.75246, 0.77086])
    T1T5_1000 = np.array([0.8203, 0.73338, 0.70922, 0.58107, 0.71025, 0.87761, 0.79125, 0.72255])
    T1T5_2000 = np.array([0.81499, 0.78228, 0.65534, 0.52541, 0.73074, 0.83445, 0.86284, 0.76615])

    T5_500 = np.array([0.81601, 0.74953, 0.64122, 0.61123, 0.7641, 0.77047, 0.74317, 0.77705])
    T5_1000 = np.array([0.76768, 0.70816, 0.57425, 0.6214, 0.76319, 0.80433, 0.68427, 0.78404])
    T5_1500 = np.array([0.76673, 0.78212, 0.61297, 0.58316, 0.74072, 0.77106, 0.78272, 0.8401])
    T5_2000 = np.array([0.75689, 0.76576, 0.66392, 0.5912, 0.77032, 0.81609, 0.73845, 0.82553])
    #
    # Coop_T5_2000 = np.array([0.78281, 0.74084, 0.68198, 0.61015, 0.74764, 0.77492, 0.81336, 0.89184])
    #
    FPT_2D = np.array([0.713, 0.714, 0.378, 0.329, 0.683, 0.667, 0.649, 0.737])
    O3Q = np.array([0.69, 0.67, 0.17, 0.32, 0.6, 0.5, 0.51, 0.67])
    Midas = np.array([0.7838, 0.66, 0.61, 0.5, 0.6466, 0.8338, 0.7314, 0.7759])
    COSMOsar3D = np.array([0.62, 0.61, 0.13, 0.43, 0.58, 0.63, 0.59, 0.66])
    #
    conf1 = "T5_2000"
    ref = T5_2000

    conf2 = "Midas"
    srT = bc.SignedRankTest(ref, Midas, rope=0.01, nsamples=500000,)
    print(srT.probs())
    srT.plot(names=(conf1, conf2))
    plt.savefig("SignedRankTest_{}_{}.png".format(conf1, conf2))
    plt.show()

    conf2 = "2D-FPT"
    srT = bc.SignedRankTest(ref, FPT_2D, rope=0.01, nsamples=500000)
    print(srT.probs())
    srT.plot(names=(conf1, conf2))
    plt.savefig("{}_{}.png".format(conf1, conf2))
    plt.show()

    conf2 = "COSMOsar3D"
    srT = bc.SignedRankTest(ref, COSMOsar3D, rope=0.01, nsamples=500000)
    print(srT.probs())
    srT.plot(names=(conf1, conf2))
    plt.savefig("{}_{}.png".format(conf1, conf2))
    plt.show()

    conf2 = "O3Q"
    srT = bc.SignedRankTest(ref, O3Q, rope=0.01, nsamples=500000)
    print(srT.probs())
    srT.plot(names=(conf1, conf2))
    plt.savefig("{}_{}.png".format(conf1, conf2))
    plt.show()

    # datas = ["anneal", "audiology", "cleeland-14", "cmc", "contact-lenses", "credit_1","credit_2", "ecoli", "eucalyptus",
    #      "german-credit", "glass", "grub-damage", "haberman", "hayes-roth", "hepatitis", "hungarian-14", "hypothyroid",
    #      "ionosphere", "iris", "kr-s-kp", "labor", "lier-disorders", "lymphography", "monks", "monks1", "monks3",
    #      "mushroom", "nursery", "optdigits", "owel", "page-blocks", "pasture-production", "pendigits", "pima-diabetes",
    #      "postoperatie", "primary-tumor", "segment", "solar-flare-C", "solar-flare-X", "solar-flare-m", "sonar",
    #      "soybean", "spambase", "spect-reordered", "splice", "squash-stored",  "squash-unstored", "tae",
    #      "waveform", "white-clover", "wine", "wisconsin-breast-cancer", "yeast", "zoo"]
    # names = ("nbc", "aode")
    # names = ("j48","j48gr")

    # difA = []
    # print(len(datas))
    # for d in datas:
    #     nbc = get_data(names[0],d)
    #     aode = get_data(names[1], d)
    #     print(d,np.subtract(nbc,aode).mean())
    #     difA.append(np.subtract(nbc,aode).mean())
    #
    # dif = np.array(difA)
    # print(len(dif))
    # print(dif.mean())

    # nbc = get_data(names[0],"hepatitis")
    # aode = get_data(names[1],"hepatitis")
    # ctT = bc.SignedRankTest(nbc,aode,rope=0.1)
    # print(ctT.probs())
    # ctT.plot(("C1","C2"))
    # # fig.show()
    # # plt.title("SignedRankTest")
    # plt.savefig("SignedRankTest_{}_{}__50000.png".format("C1","C2"))
    # plt.show()
    #

#

# ctT = bc.SignedRankTest(sha, dnn, rope=0.01)
# print(ctT.probs())
# ctT.plot(names)
# # fig.show()
# plt.title("SignedRankTest")
# plt.savefig("SignedRankTest_{}_{}__50000.png".format(names[0], names[1]))
# plt.show()
# #


# datos de cesar
# sha = np.array([0.913,0.766,0.932,0.935,0.836,0.922,0.974,0.943,0.828])
# dnn = np.array([0.874,0.629,0.914,0.937,0.854,0.847,0.944,0.927,0.886])
# sha = np.array([0.913,0.766,0.932,0.935,0.836,0.922,0.974,0.943,0.828])
# dnn = np.array([0.874,0.629,0.914,0.937,0.854,0.847,0.944,0.927,0.886])
# names = ("Shallow", "DNN")
#

# mis datos
# T5_2000_Q2 = np.array([0.75689, 0.76576, 0.66392, 0.5912, 0.77032, 0.81609, 0.73845, 0.82553])
# Coop_T5_2000_Q2 = np.array([0.76828, 0.74084, 0.68198, 0.61015, 0.74764, 0.82538, 0.81336, 0.82507])
# names = ("T5_2000", "T5_2000_Coop")
# print(T5_2000_Q2 - Coop_T5_2000_Q2)
#
# Random = np.array([0.71, 0.58887, 0.54, 0.5, 0.59, 0.69, 0.18754, 0.22])
# T1T5_500 = np.array([0.75336, 0.79385, 0.64004, 0.62851, 0.75019, 0.80813, 0.74433, 0.80335])
# T1T5_1000 = np.array([0.8203, 0.73338, 0.70922, 0.58107, 0.71025, 0.87761, 0.79125, 0.72255])
# T1T5_1500 = np.array([0.79073, 0.76489, 0.66309, 0.64565, 0.74482, 0.79619, 0.75246, 0.77086])
# T1T5_2000 = np.array([0.81499, 0.78228, 0.65534, 0.52541, 0.73074, 0.83445, 0.86284, 0.76615])
# T5_500 = np.array([0.81601, 0.74953, 0.64122, 0.61123, 0.7641, 0.77047, 0.74317, 0.77705])
# T5_1000 = np.array([0.76768, 0.70816, 0.57425, 0.6214, 0.76319, 0.80433, 0.68427, 0.78404])
# T5_1500 = np.array([0.76673, 0.78212, 0.61297, 0.58316, 0.74072, 0.77106, 0.78272, 0.8401])
# T5_2000 = np.array([0.75689, 0.76576, 0.66392, 0.5912, 0.77032, 0.81609, 0.73845, 0.82553])
#
# D2FPT = np.array([0.713, 0.714, 0.378, 0.329, 0.683, 0.667, 0.649, 0.737])
# O3Q = np.array([0.69, 0.67, 0.17, 0.32, 0.6, 0.5, 0.51, 0.67])
# Midas = np.array([0.7838, 0.66, 0.61, 0.5, 0.6466, 0.8338, 0.7314, 0.7759])
# COSMOsar3D = np.array([0.62, 0.61, 0.13, 0.43, 0.58, 0.63, 0.59, 0.66])
# names = ("Random", "T5_2000")
# ctT = bc.SignedRankTest(Random, T5_2000, rope=0.01)
# print(ctT.probs())
# ctT.plot(names)
# # fig.show()
# plt.savefig("SignedRankTest_{}_{}".format(names[0], names[1]), format="png")
# plt.show()


# T5_2000_CFS = np.array([0.9409, 0.9175, 0.8960, 0.8740, 0.9048, 0.9534, 0.9648, 0.9622])
# T5_2000_Coop_CFS = np.array([0.9445, 0.9266, 0.8541, 0.8784, 0.8950, 0.9532, 0.8897, 0.9101])


# multiple data one-dimension
# data_nbc = get_data("nbc", aggregate=True)
# data_aode = get_data("j48", aggregate=True)
# #
# names = ("nbc", "j48")
# ctT = bc.SignedRankTest(data_nbc, data_aode, rope=1)
# print(ctT.probs())
# ctT.plot(names)
# # fig.show()
# plt.title("SignedRankTest")
# # plt.savefig("SignedRankTest_{}_{}__500000.png".format(names[0], names[1]))
# plt.show()




#
# sT = bc.SignTest(data_nbc, data_aode, rope=0.01)
# print(sT.probs())
# sT.plot_simplex(names)
# plt.title("SignedTest")
# plt.show()
#
# # multiple data two-dimension
# data_nbc = get_data("nbc")
# data_aode = get_data("aode")
#
# hT = bc.HierarchicalTest(data_nbc, data_aode, rope=0.01)
# print(hT.probs())
# hT.plot_simplex(names)
# plt.title("HierarchicalTest")
# plt.show()
