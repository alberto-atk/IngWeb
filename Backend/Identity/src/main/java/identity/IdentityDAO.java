/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package identity;

import db.UserDB;
import java.util.GregorianCalendar;

/**
 *
 * @author alberto
 */
public interface IdentityDAO {
    void createUser(UserDB _user);
    String generateRandomString();
    String getSHA256(String _txt);

    RESTuser getUser(String _token, Long actualDate);

    void changePassword(String _token, String _newClearPwd, Long actualDate);

    String getToken(String _login, String _password, Long actualDate);

    void cancelToken(String _token);
}
