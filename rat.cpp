#include<iostream>
using namespace std;

int yes(int **ar,int x,int y,int n){
    if(x<n && y<n && ar[x][y]==1)
    return 1;
    return 0;
}

int rat(int** ar ,int x,int y,int n,int** ans){
    if(x==n-1 && y==n-1)
    {
        ans[x][y]=1;
        return 1;
    }
    if(yes(ar,x,y,n)){
        ans[x][y]=1;
        if(rat(ar,x+1,y,n,ans))
        return 1;
        if(rat(ar,x,y+1,n,ans))
        return 1;
        ans[x][y]=0;
        return 0;
    }
    return 0;

}

int main(){
    int n=4;
    int** ar,**ans;
    ar=new int *[n];
ans=new int *[n];



    for(int i=0;i<n;i++){
ar[i]=new int[n];
ans[i]=new int[n];
        for(int j=0;j<n;j++){
            cout<<"enter..";
            cin>>ar[i][j];
            ans[i][j]=0;
        }
    }
    rat(ar,0,0,n,ans);
    for(int i=0;i<n;i++){
    for(int j=0;j<n;j++)
    cout<<ar[i][j];
    cout<<endl;
}
for(int i=0;i<n;i++){
    for(int j=0;j<n;j++)
    cout<<ans[i][j];
    cout<<endl;
}
return 0;
}