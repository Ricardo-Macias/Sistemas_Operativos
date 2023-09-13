
package practica_figuras;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JTextField;


public class Practica_Figuras extends JFrame implements ActionListener {
    
    JLabel lblBase, lblAltura, lblArea;
    JTextField txtBase, txtAltura, txtArea;
    JComboBox cbOpcion;
    JButton btnCalcular;
    
    
    public Practica_Figuras(){
        this.setBounds(0,0,400,400);
        
        lblBase = new JLabel();
        lblBase.setBounds(10,20,100,20);
        lblBase.setName("lblBase");
        lblBase.setText("Ingresar Base: ");
        lblBase.setVisible(true);
        this.add(lblBase);
        
        txtBase = new JTextField();
        txtBase.setBounds(120, 20,100,20);
        txtBase.setName("txtBase");
        txtBase.setText("");
        txtBase.setVisible(true);
        this.add(txtBase);
        
        
        lblAltura = new JLabel();
        lblAltura.setBounds(10,50,100,20);
        lblAltura.setName("lblAltura");
        lblAltura.setText("Ingresar Altura: ");
        lblAltura.setVisible(true);
        this.add(lblAltura);
        
        txtAltura = new JTextField();
        txtAltura.setBounds(120, 50,100,20);
        txtAltura.setName("txtAltura");
        txtAltura.setText("");
        txtAltura.setVisible(true);
        this.add(txtAltura);
        
        lblArea = new JLabel();
        lblArea.setBounds(10,90,100,20);
        lblArea.setName("lblArea");
        lblArea.setText("Ingresar Area: ");
        lblArea.setVisible(true);
        this.add(lblArea);
        
        txtArea = new JTextField();
        txtArea.setBounds(120, 90,100,20);
        txtArea.setName("txtArea");
        txtArea.setText("");
        txtArea.setVisible(true);
        this.add(txtArea);
        
        btnCalcular = new JButton();
        btnCalcular.setBounds(120, 150,100,20);
        btnCalcular.setName("btnCalcular");
        btnCalcular.setText("Calcular Area");
        btnCalcular.setVisible(true);
        btnCalcular.addActionListener(this);
        this.add(btnCalcular);
        
        
        
        this.setLayout(null);
        this.setVisible(true);
    }


    public static void main(String[] args) {
        Practica_Figuras ob = new Practica_Figuras();
        ob.setVisible(true);
        
    }

    public void actionPerformed(ActionEvent e) {
        if(e.getSource() == btnCalcular){
            JOptionPane.showMessageDialog(rootPane, "Hola");
        }
    }
    
}
