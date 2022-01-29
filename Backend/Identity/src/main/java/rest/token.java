/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package rest;

import db.UserDB;
import identity.IdentityDAO;
import identity.IdentityStore;
import common.RESTuser;
import java.util.Calendar;
import java.util.Date;
import java.util.GregorianCalendar;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.UriInfo;
import javax.ws.rs.Produces;
import javax.ws.rs.Consumes;
import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.PUT;
import javax.enterprise.context.RequestScoped;
import javax.ws.rs.DELETE;
import javax.ws.rs.PathParam;
import javax.ws.rs.core.MediaType;

/**
 * REST Web Service
 *
 * @author alberto
 */
@Path("token")
@RequestScoped
public class token {

    @Context
    private UriInfo context;
    private IdentityDAO identityStore = IdentityStore.getInstance();


    /**
     * Creates a new instance of user
     */
    public token() {
    }

    
    @GET
    @Path ("{login}/{password}")
    public String getToken(@PathParam("login") String _login, @PathParam("password") String _password) {
        System.out.println("GET token");
        return identityStore.getToken(_login,identityStore.getSHA256(_password), System.currentTimeMillis());
    }
    
    
    @DELETE
    @Path ("{token}")
    public void cancelToken(@PathParam("token") String _token){
        System.out.println("DELETE cancelToken() ");
        identityStore.cancelToken(_token);
    }
}
