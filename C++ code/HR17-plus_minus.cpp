//program to calculate the fraction of positive,negative and 0 elements in an aaray
// fixed alongwith setprecision(val) is used to set the precision of the floating point number upto the given val in the bracket of setprecision.
//floor and ceil functions are used to print the box and the ceiling value of the given floating point number.
#include <bits/stdc++.h>

using namespace std;

vector<string> split_string(string);

// Complete the plusMinus function below.
void plusMinus(vector<int> arr) 
{   int p=0,n=0,nil=0;
    for(int i=0;i<arr.size();i++)
    {
        if(arr[i]>0){++p;}
        if(arr[i]<0){++n;}
        if(arr[i]==0){nil++;}
    }
    cout<<fixed<<setprecision(6)<<(float)p/arr.size()<<endl<<(float)n/arr.size()<<endl<<(float)nil/arr.size();


}

int main()
{
    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    string arr_temp_temp;
    getline(cin, arr_temp_temp);

    vector<string> arr_temp = split_string(arr_temp_temp);

    vector<int> arr(n);

    for (int i = 0; i < n; i++) {
        int arr_item = stoi(arr_temp[i]);

        arr[i] = arr_item;
    }

    plusMinus(arr);

    return 0;
}

vector<string> split_string(string input_string) {
    string::iterator new_end = unique(input_string.begin(), input_string.end(), [] (const char &x, const char &y) {
        return x == y and x == ' ';
    });

    input_string.erase(new_end, input_string.end());

    while (input_string[input_string.length() - 1] == ' ') {
        input_string.pop_back();
    }

    vector<string> splits;
    char delimiter = ' ';

    size_t i = 0;
    size_t pos = input_string.find(delimiter);

    while (pos != string::npos) {
        splits.push_back(input_string.substr(i, pos - i));

        i = pos + 1;
        pos = input_string.find(delimiter, i);
    }

    splits.push_back(input_string.substr(i, min(pos, input_string.length()) - i + 1));

    return splits;
}
