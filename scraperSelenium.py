

TODO:
SALTAR EL BUSQUEDA ESTA MUY LARGA DESEA CONTINUAR
VER SYLLABUS - Y DEVOLVERSE
CREAR BUCLES...
-------------------------------------

# download driver https://github.com/mozilla/geckodriver/releases
#add to path the driver: export PATH=$PATH:/Users/dani/Desktop/universidad/geckodriver
# instalar firefox

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

#driver = webdriver.Firefox()

class Navegador:
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=r'/Users/dani/Desktop/universidad/geckodriver')
    def ejecutar(self):
        self.__navegar("https://csg.javeriana.edu.co/psc/CS92GST/EMPLOYEE/SA/c/ESTABLISH_COURSES.CLASS_SEARCH.GBL")
        ############## selecciona configuraciones basicas
        # selecciona ciclo
        self.__selecciona_ciclo_javeriana("2230")
        # selecciona unidad academica (Direccion)
        self.__elegir_direccionAcademica("ANESTES")
        ## quita el 'ver solo clases con inscripciones abiertas'
        self.__deselect_inscripcionesAbiertas_javeriana()
        ## Click en buscar
        self.__click_buscar_javeriana()
        ## Descarga html 
        # self.descargar("page.html")

        # ## volver a modificar busqueda
        # self.__modificar_busqueda_javeriana()
        # self.__elegir_direccionAcademica("ANESTES")
        # self.__click_buscar_javeriana()
        numerosClases = self.__obtenerNumerosClases_javeriana()
        self.__entrarDetallesClase_javeriana(numerosClases[0])
        #### Para test, no cierra el navegador de inmediato
        self.__esperar(EC.presence_of_element_located((By.ID, 'dsfkajlkjfadsñ$31$_LBL')),)
        

    def __navegar(self, url):
        self.driver.get(url)

    def descargar(self, path):
        with open(path, 'w+') as f:
            f.write(self.driver.page_source)

    def __esperar_javeriana(self):
        ## verifica que la pagina no tenga la rueda de cargando
        self.__esperar(EC.invisibility_of_element_located((By.ID, 'WAIT_win0')),)

    def __modificar_busqueda_javeriana(self):
        self.__esperar_javeriana()
        buscar = self.driver.find_element(By.XPATH, '//*[@id="CLASS_SRCH_WRK2_SSR_PB_MODIFY"]')
        buscar.click()
        


    def __selecciona_ciclo_javeriana(self, ciclo):
        self.__esperar_javeriana()
        ciclo_dropdown = self.driver.find_element(By.XPATH, '//*[@id="CLASS_SRCH_WRK2_STRM$35$"]')
        all_options = ciclo_dropdown.find_elements(By.TAG_NAME, "option")
        for option in all_options:
            value = option.get_attribute("value")
            print("Value is: %s" % value)
            if(value == ciclo):
                option.click()
                break

    def __elegir_direccionAcademica(self, direccion):
        print("Unidad Academicas")
        self.__esperar_javeriana()
        direccion_dropdown = self.driver.find_element(By.XPATH, '//*[@id="SSR_CLSRCH_WRK_SUBJECT_SRCH$2"]')
        all_options = direccion_dropdown.find_elements(By.TAG_NAME, "option")
        for option in all_options:
            value = option.get_attribute("value")
            print("Value is: %s" % value)
            if(value == direccion):
                option.click()
                break
        print("fin unidad academicas")
    def __deselect_inscripcionesAbiertas_javeriana(self):
        self.__esperar_javeriana()
        selector = self.driver.find_element(By.XPATH, '//*[@id="SSR_CLSRCH_WRK_SSR_OPEN_ONLY$4"]')
        selector.click()
    def __click_buscar_javeriana(self):
        self.__esperar_javeriana()
        buscar = self.driver.find_element(By.XPATH, '//*[@id="CLASS_SRCH_WRK2_SSR_PB_CLASS_SRCH"]')
        buscar.click()
    def __obtenerNumerosClases_javeriana(self):
        print("Clases")
        self.__esperar_javeriana()
        clases = self.driver.find_elements(By.XPATH, '//*[@title="Nº Clase"]')
        numerosClases = []
        for option in clases:
            # value = option.find_element(By.XPATH, './/a[1]').text
            # value = option.get_attribute("value")
            value = option.text
            print("Value is: %s" % value)
            numerosClases.append(value)
            # if(value == direccion):
            #     option.click()
            #     break
        print("fin clases")
        return numerosClases

    def __entrarDetallesClase_javeriana(self,numeroClase):
        print("Entrar Clase")
        self.__esperar_javeriana()
        clases = self.driver.find_elements(By.XPATH, '//*[@title="Nº Clase"]')
        for option in clases:
            value = option.text
            if(value == numeroClase):
                option.click()
                break

        ## verificar que se halla saltado busqueda muy larga

        
        print("fin clase")





    def __esperar(self, *args):
        # espera por situaciones como: EC.presence_of_element_located((By.ID, 'CLASS_SRCH_WRK2_INSTITUTION$31$_LBL')),
        # se pueden añadir varias situaciones ejm:
        # self.__esperar(
        #     EC.presence_of_element_located((By.ID, 'CLASS_SRCH_WRK2_INSTITUTION$31$_LBL')),
        #     EC.presence_of_element_located((By.ID, 'lkjkjh'))
        # )
        timeout = 80
        try:
            element_present = EC.any_of(*args)
            WebDriverWait(self.driver, timeout).until(element_present)
        except TimeoutException:
            print ("Timed out waiting for page to load")

    def close(self):
        self.driver.close

p1 = Navegador()
p1.ejecutar()
p1.close()




