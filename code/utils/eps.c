#include <stdio.h>

double eps(double x) {
	unsigned long long i = *(unsigned long long*) &x;
	i++;
	double x_next = *(double*) &i;
	return x_next - x;
}

int main(void) {
	int to_secs = 24 * 60 * 60;
	double HJD_m = 5262.50650;
	double HJD = HJD_m + 2450000.0;
	double HJD_seconds = HJD * to_secs;
	double HJD_m_seconds = HJD_m * to_secs;
	
	printf("HJD:          %e (days), eps: %e (days), %e (s)\n", HJD,eps(HJD), eps(HJD)*to_secs);
	printf("              %e (s),    eps: %e (days), %e (s)\n", HJD_seconds, eps(HJD_seconds)/to_secs, eps(HJD_seconds));
	printf("HJD - 2.45e6: %e (days), eps: %e (days), %e (s)\n", HJD_m,eps(HJD_m), eps(HJD_m)*to_secs);
	printf("              %e (s),    eps: %e (days), %e (s)\n", HJD_m_seconds, eps(HJD_m_seconds)/to_secs, eps(HJD_m_seconds));
	
	return 0;
}