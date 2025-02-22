import java.util.Scanner;

public class MatrixOperations {
    public static void main(String[] args) {
        Scanner hafıza=new Scanner(System.in);
        System.out.println("Kontrol etmek istediğiniz sayıyı giriniz.");
        int i= hafıza.nextInt();
        int t=i, k=i, toplam=0, n=0;
        do {
            k=k/10;
            n+=1;
        }
        while (k>0);
        do {
            int m=t%10;
            int çarpım=1;
            for (int l=1; l<=n; l++){
                çarpım*=m;
            }
            toplam+=çarpım;
        }
        while (t>=0);
        if (toplam==i){
            System.out.println("Grilen sayı armstrong sayıdır.");
        }
        else {
            System.out.println("Girilen sayı armstrong sayı değildir.");
        }
    }
}
