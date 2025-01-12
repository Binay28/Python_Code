/*q->no. fo lines that will be inserted
stud.find() to get the reference of the required key
stud.erase() to erase value 
stud.insert(make_pair()) to insert values into map
stud[str] to print the value at the key str*/
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <map>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    int q,t=0,val;
    string str;
    cin>>q;
    map<string,int> stud;
    map<string, int>::iterator itr;
    for (int i = 0; i < q; i++) {
      cin >> t;
      if (t == 1) {
        cin >> str >> val;
        itr=stud.find(str);
        if(itr!=stud.end())
        {
            itr->second+=val;
        }
        else
        {stud.insert(make_pair(str, val));}
      }
      if(t==2)
      {
          cin>>str;
          stud.erase(str);
      }
      if (t == 3) {
        cin >> str;
        //itr=stud.find(str);
        //cout<<itr->second;
        cout<<stud[str]<<endl;
      }
    }
    return 0;
}



