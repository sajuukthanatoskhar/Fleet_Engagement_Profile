import matplotlib.pyplot


def plot_weapon_ecm_repper_profile(weapon_to_be_plotted,plt, fig, is_weapon=True) -> matplotlib.pyplot:

    ax = fig.add_subplot(111)

    distances = [0,
                 weapon_to_be_plotted.optimal,
                 weapon_to_be_plotted.optimal + weapon_to_be_plotted.falloff * 0.5,
                 weapon_to_be_plotted.optimal + weapon_to_be_plotted.falloff * 0.75,
                 weapon_to_be_plotted.optimal + weapon_to_be_plotted.falloff * 1,
                 weapon_to_be_plotted.optimal + weapon_to_be_plotted.falloff * 1.25,
                 weapon_to_be_plotted.optimal + weapon_to_be_plotted.falloff * 1.5,
                 weapon_to_be_plotted.optimal + weapon_to_be_plotted.falloff * 2]
    DPS_list = [weapon_to_be_plotted.weapon_calculate_distance_damage(distance=distance) for distance in distances]

    dps_labels = [distances[0],
                  distances[1],
                  distances[4]
                  ] # for limiting the number of labels

    dps_spread = str([int(value) for key, value in weapon_to_be_plotted.dps_spread.items()])
    radianpersec = weapon_to_be_plotted.optimalSigRadius*weapon_to_be_plotted.tracking/40000000

    plt.plot(distances, DPS_list, label="{}:{} DPS {}[EM,TH,KI,EX]\nTrk:{}rad/s ".format(weapon_to_be_plotted.ammo_name, int(weapon_to_be_plotted.dps), str(dps_spread), radianpersec))
    plt.legend(loc="upper right")
    for xy in zip(distances, DPS_list):
        if (xy[0] == weapon_to_be_plotted.optimal and is_weapon):
            ax.annotate('%d DPS@%.00f km\n%d alpha\nMAXTranVel\n%dm/s'% (xy[1], xy[0] / 1000, int(xy[1]*weapon_to_be_plotted.volley/weapon_to_be_plotted.dps), radianpersec*xy[0]), xy=xy, textcoords='data', horizontalalignment='left')
        else:
            ax.annotate('%d DPS@%.00f km\n%d alpha\nMAXTranVel\n %dm/s' % (xy[1], xy[0] / 1000, int(xy[1]*weapon_to_be_plotted.volley/weapon_to_be_plotted.dps),radianpersec*xy[0]), xy=xy, textcoords='data')


    return plt
