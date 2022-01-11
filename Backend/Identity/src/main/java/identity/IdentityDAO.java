/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package identity;

import db.UserDB;

/**
 *
 * @author alberto
 */
public interface IdentityDAO {
    void createUser(UserDB _user);
    String generateRandomString();
    String getSHA256(String _txt);

    RESTuser getUser(String _token);

    void changePassword(String _token, String _newClearPwd);
}
