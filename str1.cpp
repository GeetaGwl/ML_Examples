#include<iostream>
using namespace std;
void perm(string a,int l,int r){
    if(l==r)
    cout<<a<<endl;
    else{
        for(int i=l;i<=r;i++)
        {
            swap(a[i],a[l]);
            perm(a,l+1,r);
            swap(a[i],a[l]);
        }
    }
}
int main()
{
    string str = "ABC";
    int n = str.size();
    perm(str, 0, n-1);
    return 0;
}