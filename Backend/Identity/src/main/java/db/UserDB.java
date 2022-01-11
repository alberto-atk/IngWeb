/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package db;

import com.google.gson.Gson;

/**
 *
 * @author alberto
 */
public class UserDB {
    
    private String login;
    private String name;
    private String token;
    private String password;
    
    public UserDB(String _login, String _name, String _token, String _password){
        login = _login;
        name = _name;
        token = _token;
        password = _password;
    }

    public String getLogin() {
        return login;
    }
    
    
    public String toJson(){
        Gson gson = new Gson();
        return gson.toJson(this);
    }
    
    public String getToken(){
        return token;
    }
}
