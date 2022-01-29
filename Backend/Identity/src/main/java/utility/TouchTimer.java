
package utility;

import common.StatusCode;
import common.RESTstockkService;
import java.util.Date;
import rest.ServicesDirectoryRESTclient;
import javax.ejb.Schedule;
import javax.ejb.Stateless;

/**
 *
 * @author fserna
 */
 
 
@Stateless
public class TouchTimer {

        
	/**
	
		La anotación "@Schedule" hace que el método asociado (timer) sea invocado
		todas las horas, todos los minutos en el segundo 24. 
		Mi implementación lo hace en el segundo 21, así que esto asegura que la mayor parte
		del tiempo será vuestro servicio el que sea accesible porque habréis "tapado" el mío
	*/
    @Schedule(hour="*", minute = "*", second = "24", persistent = false)
    public void timer(){
        touch(StatusCode.NOMINAL);
    }
    
    
	
	/**
		Realiza el registro en el "servicesDirectory", para ello
			A. crea un objeto RESTstockkService con los valores pertinentes:
				- nombre del servicio a registrar 
				- prefijo de la URI donde estarán disponibles las primitivas RESTstockkService
				- estado con el que aparecerá en http://155.210.71.100:8090/stockk-servicesDirectory/
			B. se realiza el registro enviando el objeto anterior a la app "servicesDirectory"
	*/
    public void touch(StatusCode _status) {
		// A.
        System.out.println("Timer: " + new Date());
        RESTstockkService service = new RESTstockkService();
		
		// ***1*** poned el nombre "oficial" de vuestro servicio
        service.setName("stockk_IDENTITY"); 
		
		// ***2*** 
		//  En vuestro caso colocad el prefijo de la URI que corresponda.
		//  Lo suyo sería obtener la URI de un fichero de configuración...
	service.setUri("http://155.210.71.106:7040/stockk_IDENTITY/rest");
       
        service.setStatus(_status);
        service.setMs(System.currentTimeMillis());
        
		// esperamos un tiempo aleatorio (máx 2") para evitar que se amontonen los
		// registros en el mismo milisegundo (y que eso genere problemas)
        long randomDelay = (int)(Math.random()*2000);
        try {
            Thread.sleep(randomDelay);
        } catch (InterruptedException ex) {
        }
		
		// B.
        ServicesDirectoryRESTclient directory = new ServicesDirectoryRESTclient();
        directory.registerService(service);
        directory.close();
    }


}
