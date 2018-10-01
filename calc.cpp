#include <iostream>
#include <tuple>
#include <math.h>

double ComputeMuE (int delta_E) {
    return (1/(1+exp(0.003*delta_E)));
}

double ComputeMuDeltaS (int delta_S) {
    int delta_S_min = 2;
    int delta_S_T = 11;

    if (delta_S < delta_S_min || delta_S > delta_S_T) {
        std::cout << "Impossible Score!!" << std::endl;
        return 0;
    }

    return abs(((-0.9) / delta_S_min) * (delta_S_T - delta_S) + 1);
}

std::tuple<int, int> ComputeNewElo (int e_A, int s_A, int e_B, int s_B) {
    int delta_E = e_A - e_B;
    int delta_S = abs(s_A - s_B);

    if (s_B > s_A) {
        delta_E *= -1;
    }

    double mu_E = ComputeMuE(delta_E);
    double mu_delta_S = ComputeMuDeltaS(delta_S);

    if (s_A > s_B) {
        e_A = int(round(e_A + (0.1 * e_A * mu_E * mu_delta_S)));
        e_B = int(round(e_B - (0.1 * e_B * mu_E * mu_delta_S)));
    } else {
        e_A = int(round(e_A - (0.1 * e_A * mu_E * mu_delta_S)));
        e_B = int(round(e_B + (0.1 * e_B * mu_E * mu_delta_S)));
    }
    return std::make_tuple(e_A, e_B);
}

int main(int argc, char *argv[]) {
    std::tuple<int, int> newElos= ComputeNewElo(std::stoi(argv[1]), std::stoi(argv[2]), std::stoi(argv[3]), std::stoi(argv[4]));
    std::cout << std::get<0>(newElos) << std::endl << std::get<1>(newElos) << std::endl;
    return 0;
}