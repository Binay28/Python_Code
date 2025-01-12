#include <bits/stdc++.h>

using namespace std;

// Complete the diagonalDifference function below.
int diagonalDifference(vector<vector<int>> arr) 
{
    vector<vector<int>>::iterator row;
    vector<int>::iterator col1,col2;
    int sd1=0,sd2=0,j=0;
    for(row=arr.begin();row!=arr.end();row++)
    {   col1=row->begin();col2=row->end();
        sd1+=*(col1+j);sd2+=*(col2-j-1);
        j++;
    }
    /*vector<vector<int>>::iterator row;
    int s=row.size();
    int sd1=0,sd2=0,j=s-1;
    for(int i=0;i<s;i++)
    {
        sd1+=arr[i][i];
        sd2+=arr[i][s];
        j--;
    }*/
    //cout<<sd1-sd2;
    return (sd1-sd2)>0?(sd1-sd2):sd2-sd1;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    vector<vector<int>> arr(n);
    for (int i = 0; i < n; i++) {
        arr[i].resize(n);

        for (int j = 0; j < n; j++) {
            cin >> arr[i][j];
        }

        cin.ignore(numeric_limits<streamsize>::max(), '\n');
    }

    int result = diagonalDifference(arr);

    fout << result << "\n";

    fout.close();

    return 0;
}
