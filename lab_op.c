#include "stdio.h"

struct circle {
    int rad;
};

struct ring {
    struct circle big, little;
};

double find_len(struct ring);

double find_s(struct ring);

int main() {
    int small;
    int big;
    scanf("%d %d", &small, &big);
    struct ring R = {big, small};

    printf("%f\n", find_len(R));
    printf("%f\n", find_s(R));

    return 0;
}