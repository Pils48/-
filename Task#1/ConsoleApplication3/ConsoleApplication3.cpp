// ConsoleApplication3.cpp: определяет точку входа для консольного приложения.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main()
{
	ifstream fin("arrival.in.txt");
	ofstream fout("arrival.out.txt", ios_base::trunc);

	int n, m, tmp;
	vector<int> buses, idxs;
	fin >> n >> m;
	while (!fin.eof()) {
		fin >> tmp;
		buses.push_back(tmp);
	}
	int Imax, max;
	int k = 0;
	tmp = 0;

	while ((k < m) && (tmp < n)) {
		max = buses[0];
		Imax = 0;
		for (int i = 0; i < buses.size(); i++) {
			if (buses[i] > max) {
				max = buses[i];
				Imax = i;
			}
		}
		tmp += max;
		k++;
		buses[Imax] = -1;
		idxs.push_back(Imax);
	}

	if (tmp < n) {
		fout << -1;
	}
	else {
		fout << k << endl;
		for (int i = 0; i < idxs.size(); i++) {
			fout << idxs[i] << " ";
		}
	}
	fin.close();
	fout.close();
    return 0;
}

