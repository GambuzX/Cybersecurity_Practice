import java.util.*;

class VaultDoor3 {

    public static void main(String[] args) {
        checkPassword();
    }
    
    // Our security monitoring team has noticed some intrusions on some of the
    // less secure doors. Dr. Evil has asked me specifically to build a stronger
    // vault door to protect his Doomsday plans. I just *know* this door will
    // keep all of those nosy agents out of our business. Mwa ha!
    //
    // -Minion #2671
    public static void checkPassword() {
        /*for (i=0; i<8; i++) {
            buffer[i] = password.charAt(i);
        }
        for (; i<16; i++) {
            buffer[i] = password.charAt(23-i);
        }
        for (; i<32; i+=2) {
            buffer[i] = password.charAt(46-i);
        }
        for (i=31; i>=17; i-=2) {
            buffer[i] = password.charAt(i);
        }*/
        
        char[] password = new char[32];
        String stuff = "jU5t_a_sna_3lpm11ga4e_u_4_m9rf48";
        int i;
        for (i = 31; i >= 17; i-=2) {
            password[i] = stuff.charAt(i);
        }
        i = 16;
        for (; i<32; i+=2) {
            password[46-i] = stuff.charAt(i);
        }
        i = 8;
        for (; i<16; i++) {
            password[23-i] = stuff.charAt(i);
        }
        for (i=0; i<8; i++) {
            password[i] = stuff.charAt(i);
        }
        
        
        String s = new String(password);
        System.out.print(s);
    }
}
