#include<stdio.h>
int sumdigits(int n)
{
    int sum = 0, m;
    while (n > 0)
    {
        m = n % 10;
        sum = sum + m;
        n = n / 10;
    }
    return sum;
}
int productdigits(int n){
    int product = 1, m;
    while (n > 0)
    {
        m = n % 10;
        product = product * m;
        n = n / 10;
    }
    return product;
}
int main()
{
    int T,A,B;
    scanf("%d",&T);
    for(int i=0;i<T;i++){
        scanf("%d %d",&A,&B);
        int count=0;
        for(int j=A;j<B+1;j++){
            if(productdigits(j)%sumdigits(j)==0){
                count++;
            }
        }
        printf("Case #%d: %d\n",i+1,count);
    }
    return 0;
}