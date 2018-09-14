#include<iostream>
#include<algorithm>
using namespace std;

int main()
{
    vector<int> v1={20,30,40,25,15};

    vector<int>::iterator it;

    make_heap(v1.begin(),v1.end());
    cout<<"The max value of the heap = ";
    cout<<v1.front()<<endl;

    //push
    v1.push_back(50);
    push_heap(v1.begin(),v1.end());
    cout<<"The max value of the heap = ";
    cout<<v1.front()<<endl;

    pop_heap(v1.begin(),v1.end());
    v1.pop_back();

    cout<<"The heap elements are :";
    for (int &x:v1)
        cout<<x<<" ";
    cout<<endl;

    sort_heap(v1.begin(),v1.end());

    cout<<"The heap elements are :";
    for (int &x:v1)
        cout<<x<<" ";
    cout<<endl;


    return 0;


}



