def game(terra, power):

    power_sum = power

    for list in terra:

        for list_power in list:

            if power_sum >= list_power:

                power_sum += list_power

            else:

                break

    return power_sum

