#include<iostream>
using namespace std;

int yes(int **ar,int x,int y,int n){
    for(int r=0;r<x;r++){
if(ar[r][y]==1){
    return 0;
}
    }
int r=x;
int c=y;
while(r>=0 && c>=0){
    if(ar[r][c]==1){
        return 0;
    }
    r--;
    c--;
}
r=x;
c=y;
while(r>=0 && c< n ){
    if(ar[r][c]==1){
        return 0;
    }
    r--;
    c++;
}
return 1;
}

int queen(int **ar,int x,int n){
    if(x>=n)
    return 1;
    for(int c=0;c<n;c++){
        if(yes(ar,x,c,n)){
            ar[x][c]=1;
if(queen(ar,x+1,n)){
return 1;
}
ar[x][c]=0;

        }
    }
    return 0;
}

int main(){
     int n=4;
    int** ar;
    ar=new int *[n];




    for(int i=0;i<n;i++){
ar[i]=new int[n];

        for(int j=0;j<n;j++){
            
           
            ar[i][j]=0;
        }
    }
    queen(ar,0,n);
    for(int i=0;i<n;i++){
    for(int j=0;j<n;j++)
    cout<<ar[i][j];
    cout<<endl;
}
return 0;
}