#include <stdio.h>

int main(void)
{
	int h = 0, m = 0, s = 0; //분과 초가 60보다 클 경우 시와 분으로 숫자가 올라감.
	int n = 0, r = 0, d = 0;
	scanf("%d %d %d", &h, &m, &s);
	scanf("%d", &n);
	if (n / 3600 > 0)
	{
		d = n / 3600;
		n = n - (3600*d);
		h = h + d;
		if (h >= 24)
		{
			h = h%24;
		}
		if (n / 60 > 0)
		{
			r = n % 60;
			n = n / 60;
			s = s + r;
			if (s >= 60)
			{
				s -= 60;
				m += 1;
			}

			m = m + n;
			if (m >= 60)
			{
				m -= 60;
				h += 1;
				if (h >= 24)
				{
					h = h%24;
				}
			}
		}
		else
		{
			r = n % 60;
			s = s + r;
			if (s >= 60)
			{
				s -= 60;
				m += 1;
			}
			if (m >= 60)
			{
				m -= 60;
				h += 1;
				if (h >= 24)
				{
					h = h%24;
				}
			}
		}
	}
	else
	{
		if (n / 60 > 0)
		{
			r = n % 60;
			n = n / 60;

			s = s + r;
			if (s >= 60)
			{
				s -= 60;
				m += 1;
			}

			m = m + n;
			if (m >= 60)
			{
				m -= 60;
				h += 1;
				if (h >= 24)
				{
					h = h%24;
				}
			}
		}
		else
		{
			r = n % 60;
			s = s + r;

			if (s >= 60)
			{
				s -= 60;
				m += 1;
			}

			if (m >= 60)
			{
				m -= 60;
				h += 1;
				if (h >= 24)
				{
					h = h%24;
				}
			}
		}
	}
	printf("%d %d %d", h, m, s);
	return 0;
}