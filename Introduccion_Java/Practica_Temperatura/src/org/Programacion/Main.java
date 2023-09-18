
package org.Programacion;

public class Main extends javax.swing.JFrame {
    
    
    Celsius c;

    public Main() {
        initComponents();
        c= new Celsius();
    }

    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        buttonGroup1 = new javax.swing.ButtonGroup();
        jLabel1 = new javax.swing.JLabel();
        jLabel2 = new javax.swing.JLabel();
        txt_valor = new javax.swing.JTextField();
        txt_Resultado = new javax.swing.JTextField();
        btn_Convertir = new javax.swing.JButton();
        rbtn_Celsius_Kelvin = new javax.swing.JRadioButton();
        rbtn_Celsius_Fahrenheit = new javax.swing.JRadioButton();
        rbtn_Kelvin_Celsius = new javax.swing.JRadioButton();
        rbtn_Kelvin_Fahrenheit = new javax.swing.JRadioButton();
        jLabel3 = new javax.swing.JLabel();
        rbtn_Fahrenheit_Celsius = new javax.swing.JRadioButton();
        rbtn_Fahrenheit_Kelvin = new javax.swing.JRadioButton();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        setMinimumSize(new java.awt.Dimension(10, 10));

        jLabel1.setText("Ingresar valor");
        jLabel1.setName(""); // NOI18N

        jLabel2.setText("Resultado");

        txt_Resultado.setEditable(false);

        btn_Convertir.setText("Convertir");
        btn_Convertir.setName("btn_Convertir"); // NOI18N
        btn_Convertir.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btn_ConvertirActionPerformed(evt);
            }
        });

        buttonGroup1.add(rbtn_Celsius_Kelvin);
        rbtn_Celsius_Kelvin.setText("Celsius-Kelvin");

        buttonGroup1.add(rbtn_Celsius_Fahrenheit);
        rbtn_Celsius_Fahrenheit.setText("Celsius-Fahrenheit");

        buttonGroup1.add(rbtn_Kelvin_Celsius);
        rbtn_Kelvin_Celsius.setText("Kelvin-Celsius");
        rbtn_Kelvin_Celsius.setToolTipText("");

        buttonGroup1.add(rbtn_Kelvin_Fahrenheit);
        rbtn_Kelvin_Fahrenheit.setText("Kelvin-Fahrenheit");

        jLabel3.setFont(new java.awt.Font("Segoe UI", 0, 24)); // NOI18N
        jLabel3.setText("Conversor entre temperaturas");

        buttonGroup1.add(rbtn_Fahrenheit_Celsius);
        rbtn_Fahrenheit_Celsius.setText("Fahrenheit-Celsius");

        buttonGroup1.add(rbtn_Fahrenheit_Kelvin);
        rbtn_Fahrenheit_Kelvin.setText("Fahrenheit-Kelvin");

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGap(30, 30, 30)
                .addComponent(jLabel3, javax.swing.GroupLayout.PREFERRED_SIZE, 340, javax.swing.GroupLayout.PREFERRED_SIZE))
            .addGroup(layout.createSequentialGroup()
                .addGap(36, 36, 36)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(layout.createSequentialGroup()
                        .addComponent(jLabel1, javax.swing.GroupLayout.PREFERRED_SIZE, 90, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addGap(4, 4, 4)
                        .addComponent(txt_valor, javax.swing.GroupLayout.PREFERRED_SIZE, 110, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addGroup(layout.createSequentialGroup()
                        .addComponent(jLabel2, javax.swing.GroupLayout.PREFERRED_SIZE, 80, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addGap(14, 14, 14)
                        .addComponent(txt_Resultado, javax.swing.GroupLayout.PREFERRED_SIZE, 110, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addGroup(layout.createSequentialGroup()
                        .addGap(54, 54, 54)
                        .addComponent(btn_Convertir, javax.swing.GroupLayout.PREFERRED_SIZE, 134, javax.swing.GroupLayout.PREFERRED_SIZE)))
                .addGap(30, 30, 30)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(rbtn_Celsius_Kelvin, javax.swing.GroupLayout.PREFERRED_SIZE, 130, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(rbtn_Celsius_Fahrenheit, javax.swing.GroupLayout.PREFERRED_SIZE, 130, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(rbtn_Kelvin_Celsius, javax.swing.GroupLayout.PREFERRED_SIZE, 130, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(rbtn_Kelvin_Fahrenheit, javax.swing.GroupLayout.PREFERRED_SIZE, 130, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(rbtn_Fahrenheit_Kelvin, javax.swing.GroupLayout.PREFERRED_SIZE, 130, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(rbtn_Fahrenheit_Celsius, javax.swing.GroupLayout.PREFERRED_SIZE, 130, javax.swing.GroupLayout.PREFERRED_SIZE)))
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGap(10, 10, 10)
                .addComponent(jLabel3, javax.swing.GroupLayout.PREFERRED_SIZE, 40, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(30, 30, 30)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(layout.createSequentialGroup()
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addGroup(layout.createSequentialGroup()
                                .addGap(1, 1, 1)
                                .addComponent(jLabel1))
                            .addComponent(txt_valor, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                        .addGap(18, 18, 18)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addGroup(layout.createSequentialGroup()
                                .addGap(1, 1, 1)
                                .addComponent(jLabel2))
                            .addComponent(txt_Resultado, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                        .addGap(48, 48, 48)
                        .addComponent(btn_Convertir, javax.swing.GroupLayout.PREFERRED_SIZE, 50, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addGroup(layout.createSequentialGroup()
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(rbtn_Celsius_Kelvin)
                            .addGroup(layout.createSequentialGroup()
                                .addGap(20, 20, 20)
                                .addComponent(rbtn_Celsius_Fahrenheit))
                            .addGroup(layout.createSequentialGroup()
                                .addGap(40, 40, 40)
                                .addComponent(rbtn_Kelvin_Celsius))
                            .addGroup(layout.createSequentialGroup()
                                .addGap(60, 60, 60)
                                .addComponent(rbtn_Kelvin_Fahrenheit)))
                        .addGap(19, 19, 19)
                        .addComponent(rbtn_Fahrenheit_Kelvin))
                    .addGroup(layout.createSequentialGroup()
                        .addGap(80, 80, 80)
                        .addComponent(rbtn_Fahrenheit_Celsius))))
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void btn_ConvertirActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btn_ConvertirActionPerformed
        if(rbtn_Celsius_Kelvin.isSelected()){
            c.setCelsius(Double.parseDouble(txt_valor.getText()));
            txt_Resultado.setText(String.valueOf(c.Celsius_Kelvin()));
        }
        else if (rbtn_Celsius_Fahrenheit.isSelected()){
            c.setCelsius(Double.parseDouble(txt_valor.getText()));
            txt_Resultado.setText(String.valueOf(c.Celsius_Fahrenheit()));
        }
    }//GEN-LAST:event_btn_ConvertirActionPerformed

    /**
     * @param args the command line arguments
     */
    public static void main(String args[]) {
        /* Set the Nimbus look and feel */
        //<editor-fold defaultstate="collapsed" desc=" Look and feel setting code (optional) ">
        /* If Nimbus (introduced in Java SE 6) is not available, stay with the default look and feel.
         * For details see http://download.oracle.com/javase/tutorial/uiswing/lookandfeel/plaf.html 
         */
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(Main.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(Main.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(Main.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(Main.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new Main().setVisible(true);
            }
        });
    }
    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton btn_Convertir;
    private javax.swing.ButtonGroup buttonGroup1;
    private javax.swing.JLabel jLabel1;
    private javax.swing.JLabel jLabel2;
    private javax.swing.JLabel jLabel3;
    private javax.swing.JRadioButton rbtn_Celsius_Fahrenheit;
    private javax.swing.JRadioButton rbtn_Celsius_Kelvin;
    private javax.swing.JRadioButton rbtn_Fahrenheit_Celsius;
    private javax.swing.JRadioButton rbtn_Fahrenheit_Kelvin;
    private javax.swing.JRadioButton rbtn_Kelvin_Celsius;
    private javax.swing.JRadioButton rbtn_Kelvin_Fahrenheit;
    private javax.swing.JTextField txt_Resultado;
    private javax.swing.JTextField txt_valor;
    // End of variables declaration//GEN-END:variables
}
