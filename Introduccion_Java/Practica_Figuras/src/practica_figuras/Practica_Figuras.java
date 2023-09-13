
package practica_figuras;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JFrame;


public class Practica_Figuras extends JFrame implements ActionListener {
    
    public Practica_Figuras(){
        this.setBounds(0,0,400,400);
        this.setLayout(null);
        this.setVisible(true);
    }


    public static void main(String[] args) {
        Practica_Figuras ob = new Practica_Figuras();
        ob.setVisible(true);
        
    }

    public void actionPerformed(ActionEvent e) {
        throw new UnsupportedOperationException("Not supported yet.");
    }
    
}
