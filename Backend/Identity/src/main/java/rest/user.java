/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package rest;

import db.UserDB;
import identity.IdentityDAO;
import identity.IdentityStore;
import identity.RESTuser;
import java.util.GregorianCalendar;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.UriInfo;
import javax.ws.rs.Produces;
import javax.ws.rs.Consumes;
import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.PUT;
import javax.enterprise.context.RequestScoped;
import javax.ws.rs.POST;
import javax.ws.rs.PathParam;
import javax.ws.rs.core.MediaType;

/**
 * REST Web Service
 *
 * @author alberto
 */
@Path("user")
@RequestScoped
public class user {

    @Context
    private UriInfo context;
    
    private IdentityDAO identityStore = IdentityStore.getInstance();


    public user() {
    }
    
    
    @POST
    @Path ("{password}")
    public void createUser(RESTuser _user, @PathParam("password") String _password) {
        String encodedPassword = identityStore.getSHA256(_password);
        String token = identityStore.generateRandomString();
        UserDB user = new UserDB(_user.getLogin(),_user.getName(),
                        token, encodedPassword);
        identityStore.createUser(user);
    }

    /**
     * Retrieves representation of an instance of rest.user
     * @return an instance of java.lang.String
     */
    @GET
    @Path ("{token}")
    public RESTuser getUser(@PathParam("token") String _token) {
        return identityStore.getUser(_token, System.currentTimeMillis());
    }

    /**
     * PUT method for updating or creating an instance of user
     * @param content representation for the resource
     */
    @PUT
    @Path ("{token}&{newClearPwd}")
    public void changePassword(@PathParam("token") String _token, @PathParam("newClearPwd") String _newClearPwd) {
        identityStore.changePassword(_token,identityStore.getSHA256(_newClearPwd), System.currentTimeMillis());
    }
    

}
