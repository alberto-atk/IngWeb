/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package db;

import com.google.gson.Gson;
import static java.time.Clock.system;
import java.util.Calendar;
import java.util.Date;
import java.util.GregorianCalendar;

/**
 *
 * @author alberto
 */
public class UserDB {
    
    private String login;
    private String name;
    private String token;
    private String password;
    private Long timeStampTokenInMs;
    
    
    public UserDB(String _login, String _name, String _token, String _password){
        login = _login;
        name = _name;
        token = _token;
        password = _password;
        timeStampTokenInMs = System.currentTimeMillis();
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

    public String getName() {
        return name;
    }

    public Long getTimeStampToken() {
        return timeStampTokenInMs;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public boolean equalsPasswords(String _password){
        return this.password.equals(_password);
    }

    public void setToken(String token) {
        this.token = token;
    }
    
    public void setTimeStampToken(Long _timeStampToken) {
        this.timeStampTokenInMs = _timeStampToken;
    }
    
    public boolean tokenExpired(Long _timeStampToken){
        Date dateMinus5Minutes = new Date(_timeStampToken - (5*60*1000));
        GregorianCalendar aux = new GregorianCalendar();
        aux.setTime(dateMinus5Minutes);
        GregorianCalendar timeInBd = new GregorianCalendar();
        timeInBd.setTimeInMillis(timeStampTokenInMs);
        return timeInBd.before(aux);
    }

}
