#include <iostream>
using namespace std;

void input(int &row, int &colmn, int arr[100][100]) {
    cout << "row: "; cin >> row;
    cout << "colmn: "; cin >> colmn;
    for (int i = 0; i < row; i++) {
        for (int j = 0; j < colmn; j++) {
            cout << "input arr[" << i << "][" << j << "] = ";
            cin >> arr[i][j];
        }
    }
}

void output(int row, int colmn, int arr[100][100]) {
    cout << endl << "output array:" << endl;
    for (int i = 0; i < row; i++) {
        for (int j = 0; j < colmn; j++) {
            cout << arr[i][j] << " ";
        }
        cout << endl;
    }
}

int main() {
    // int row;
    // int colmn;
    // int arr[100][100];

    // input(row, colmn, arr);
    // output(row, colmn, arr);

    cout << "true: " << true << endl;
    cout << "false: " << false << endl;
}