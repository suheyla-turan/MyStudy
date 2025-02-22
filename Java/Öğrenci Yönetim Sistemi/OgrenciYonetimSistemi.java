import javax.swing.*;


public class OgrenciYonetimSistemi {
    public static void main(String[] args) {
        int ogrenciSayisi = Integer.parseInt(JOptionPane.showInputDialog("Kaç öğrenci bilgisi gireceksiniz?"));

        StringBuilder hafiza = new StringBuilder();
        hafiza.append("Girilen Öğrenci Bilgileri:\n");

        for (int i = 0; i < ogrenciSayisi; i++) {
            JTextField adField = new JTextField(25);
            JTextField soyadField = new JTextField(25);
            JTextField ogrenciNoField = new JTextField(25);
            JTextField bolumField = new JTextField(25);
            JTextField yilField = new JTextField(25);
            JTextField bolumyilField = new JTextField(25);


            JPanel panel = new JPanel();
            panel.setLayout(new BoxLayout(panel, BoxLayout.Y_AXIS));
            panel.add(new JLabel("Ad:"));
            panel.add(adField);
            panel.add(new JLabel("Soyad:"));
            panel.add(soyadField);
            panel.add(new JLabel("Öğrenci No:"));
            panel.add(ogrenciNoField);
            panel.add(new JLabel("Bölümü:"));
            panel.add(bolumField);
            panel.add(new JLabel("Giriş Yılı:"));
            panel.add(yilField);
            panel.add(new JLabel(" Bölüm Kaç Yıllık ?:"));
            panel.add(bolumyilField);

            int result = JOptionPane.showConfirmDialog(null, panel,
                    "Öğrenci Bilgilerini Girin", JOptionPane.OK_CANCEL_OPTION);

            if (result == JOptionPane.OK_OPTION) {

                String ad = adField.getText();
                String soyad = soyadField.getText();
                long ogrenciNo = Long.parseLong(ogrenciNoField.getText());
                String bolum = bolumField.getText();
                int yil=Integer.parseInt(yilField.getText());
                int bolumyil=Integer.parseInt(bolumyilField.getText());


                hafiza.append(i+1+". ÖĞRENCİ").append("\n");
                hafiza.append("Ad: ").append(ad).append("\n");
                hafiza.append("Soyad: ").append(soyad).append("\n");
                hafiza.append("Öğrenci No: ").append(ogrenciNo).append("\n");
                hafiza.append("Bölüm: ").append(bolum).append("\n");
                hafiza.append("Tahmini Mezuniyet Tarihi: ").append(hesaplaMezuniyet(yil,bolumyil
                )).append("\n \n");
            } else {
                break; // İptal edilirse döngüyü sonlandır
            }
        }

        JOptionPane.showMessageDialog(null, hafiza.toString(),"SONUÇ",JOptionPane.INFORMATION_MESSAGE);
    }
    public static int hesaplaMezuniyet(int yil,int bolumyil){
        int i= yil+bolumyil;
        return i;
    }
}
