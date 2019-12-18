import flask, requests, json, math
from flask import request, jsonify, render_template

from HeuristicFactory import HeuristicFactory
from FunctionFactory import FunctionFactory

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return render_template('template.html')

#A route to return a particular book given an id value
@app.route('/api/resources/genetic', methods=['GET'])
def fact():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.

    #/api/resources/genetic?heuristica=ECLECTIC&funcion=sen(x)&precision=10&semilla=2&iteraciones=10000&maximizar=1&rangoInicial=0&rangoFinal=6.28&poblacion=200&pCruce=0.9&pMutacion=0.01
    if 'heuristica' in request.args:
        heuristica = str(request.args['heuristica'])
    else:
        return "Error: No se ha declarado la heurística."

    if 'funcion' in request.args:
        funcion = str(request.args['funcion'])
    else:
        return "Error: No se ha declarado la función."

    if 'precision' in request.args:
        precision = int(request.args['precision'])
    else:
        return "Error: No se ha declarado la precisión."

    if 'semilla' in request.args:
        semilla = int(request.args['semilla'])
    else:
        return "Error: No se ha declarado la semilla."

    if 'iteraciones' in request.args:
        iteraciones = int(request.args['iteraciones'])
    else:
        return "Error: No se han declarado las iteraciones."

    if 'maximizar' in request.args:
        maximizar = int(request.args['maximizar'])
    else:
        return "Error: No se ha declarado la optimización."

    if 'rangoInicial' in request.args:
        rangoInicial = float(request.args['rangoInicial'])
    else:
        return "Error: No se ha declarado el rangoInicial."

    if 'rangoFinal' in request.args:
        rangoFinal = float(request.args['rangoFinal'])
    else:
        return "Error: No se ha declarado el rangoFinal."

    if 'Opfuncion' in request.args:
        opFuncion = request.args['Opfuncion']
    else:
        return "Error."

    funciones = FunctionFactory()

    if opFuncion == "Hansen":
        f = funciones.getHeuristic("HANSEN",rangoInicial,rangoFinal)
    elif opFuncion == "DeJong":
        f = funciones.getHeuristic("DEJONG",rangoInicial,rangoFinal,2)
    elif opFuncion == "AxisParallel":
        f = funciones.getHeuristic("AXISPARALLEL",rangoInicial,rangoFinal,2)
    elif opFuncion == "RotatedHyper":
        f = funciones.getHeuristic("ROTATEDHYPER",rangoInicial,rangoFinal,2)
    else:
        funcion = funcion.replace(" ","+")
        f = funciones.getHeuristic("POLINOMIO",rangoInicial,rangoFinal,0,funcion)

    if maximizar == 1:
        maximizar = True
    else:
        maximizar = False

    hf = HeuristicFactory(f)

    if heuristica == "ECLECTIC":
        if 'poblacion' in request.args:
            poblacion = int(request.args['poblacion'])
        else:
            return "Error: No se ha declarado la población."

        if 'pCruce' in request.args:
            pCruce = float(request.args['pCruce'])/100
        else:
            return "Error: No se ha declarado la probabilidad de cruce."

        if 'pMutacion' in request.args:
            pMutacion = float(request.args['pMutacion'])/100
        else:
            return "Error: No se ha declarado la probabilidad de mutación."
        variables,valoresFuncion = hf.getHeuristic(heuristica, maximizar, poblacion, pMutacion, pCruce).execute(precision,semilla,iteraciones)
    else:
        variables,valoresFuncion = hf.getHeuristic(heuristica, maximizar).execute(precision,semilla,iteraciones)
    
    return jsonify(variables=variables, valores=valoresFuncion, funcion=funcion)

@app.route('/resultados', methods=['GET'])
def res():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in     the browser.
    if 'heuristica' in request.args:
        heuristica = (request.args['heuristica'])
    else:
        return "Error: No se ha declarado la heurística."

    if 'funcion' in request.args:
        funcion = (request.args['funcion'])
    else:
        return "Error: No se ha declarado la función."

    if 'precision' in request.args:
        precision = (request.args['precision'])
    else:
        return "Error: No se ha declarado la precisión."

    if 'semilla' in request.args:
        semilla = (request.args['semilla'])
    else:
        return "Error: No se ha declarado la semilla."

    if 'iteraciones' in request.args:
        iteraciones = (request.args['iteraciones'])
    else:
        return "Error: No se han declarado las iteraciones."

    if 'maximizar' in request.args:
        maximizar = (request.args['maximizar'])
    else:
        return "Error: No se ha declarado la optimización."

    if 'rangoInicial' in request.args:
        rangoInicial = (request.args['rangoInicial'])
    else:
        return "Error: No se ha declarado el rangoInicial."

    if 'rangoFinal' in request.args:
        rangoFinal = (request.args['rangoFinal'])
    else:
        return "Error: No se ha declarado el rangoFinal."

    if 'Opfuncion' in request.args:
        opFuncion = request.args['Opfuncion']
    else:
        return "Error."

    parametros = "?Opfuncion="+opFuncion+"&heuristica="+heuristica+"&funcion="+funcion+"&precision="+precision+"&semilla="+semilla+"&iteraciones="+iteraciones+"&maximizar="+maximizar+"&rangoInicial="+rangoInicial+"&rangoFinal="+rangoFinal

    if heuristica == "ECLECTIC":
        if 'poblacion' in request.args:
            poblacion = (request.args['poblacion'])
        else:
            return "Error: No se ha declarado la población."

        if 'pCruce' in request.args:
            pCruce = (request.args['pCruce'])
        else:
            return "Error: No se ha declarado la probabilidad de cruce."

        if 'pMutacion' in request.args:
            pMutacion = (request.args['pMutacion'])
        else:
            return "Error: No se ha declarado la probabilidad de mutación."

        parametros = parametros + "&poblacion="+poblacion+"&pCruce="+pCruce+"&pMutacion="+pMutacion
    
    info = requests.get('http://localhost:5000/api/resources/genetic'+parametros)
    result = json.loads(info.content)
    pfuncion = result["funcion"].replace("+","&#43;")

    return render_template('resultados.html', variables=result["variables"], valores=result["valores"],funcion=result["funcion"])

app.run()
