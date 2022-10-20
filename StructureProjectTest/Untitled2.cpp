#include<iostream>
 
using namespace std;
 
typedef char ElemType;
 
typedef struct BiTNode{
    ElemType data;
    struct BiTNode *lchild,*rchild;
}BiTNode,*BiTree;
 
bool InitBiTree(BiTree& T); //初始化
int treeDepth(BiTree T);   //计算树的深度
 
bool InitBiTree(BiTree& T){
    ElemType ch;
    cin>>ch;
    if(ch=='#'){
        T = NULL;
    }else{
        T = (BiTNode*)malloc(sizeof(BiTNode));
        T->data = ch;
        InitBiTree(T->lchild);
        InitBiTree(T->rchild);
    }
}
 
int treeDepth(BiTree T){
    if(T==NULL) return 0;
    int l = treeDepth(T->lchild);
    int r = treeDepth(T->rchild);
    return l>r?l+1:r+1;
}
 
void test(){
    BiTree T;
    InitBiTree(T);
 
    cout<<treeDepth(T);
}
 
int main(){
 
    test();
    return 0;
}
/*
输入样例：
ABD##E##C##
输出样例：
3
*/
