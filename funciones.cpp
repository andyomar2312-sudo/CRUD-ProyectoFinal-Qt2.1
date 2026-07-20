#include "funciones.h"
#include <QFile>
#include <QTextStream>
QString ruta="inventario.txt";

void guardar(const QVector<Producto>& lista){
    QFile archivo(ruta);
    if(!archivo.open(QIODevice::WriteOnly|QIODevice::Text))
        return;
    QTextStream salida(&archivo);
    for(Producto p: lista){
        salida<<p.codigo<<";"<<p.nombre<<";"<<p.tipo<<";"<<p.precio<<";"<<p.anio<<"\n";
    }
    archivo.close();
}

void leer(QVector<Producto>& lista){
    lista.clear();
    QFile archivo(ruta);
    if(!archivo.open(QIODevice::ReadOnly|QIODevice::Text))
        return;
    QTextStream entrada(&archivo);
    while (!entrada.atEnd()) {
        QString linea = entrada.readLine();
        QStringList datos = linea.split(";");
        if(datos.size()==5){
            Producto p;
            p.codigo=datos[0];
            p.nombre=datos[1];
            p.tipo=datos[2];
            p.precio=datos[3].toDouble();
            p.anio=datos[4].toInt();
            lista.push_back(p);
        }
    }
    archivo.close();
}

void crear(QVector<Producto>& lista, const Producto& nuevo){
    lista.push_back(nuevo);
    guardar(lista);
}

bool modificar(QVector<Producto>& lista, const QString& codigo, const Producto& nuevo){
    int pos= buscar(lista, codigo);
    if(pos==-1)
        return false;
    lista[pos]=nuevo;
    guardar(lista);
    return true;
}

int buscar (QVector<Producto>& lista, const QString& codigo){
    for(int i=0;i<lista.size();i++){
        if(lista[i].codigo==codigo)
            return i;
    }
    return -1;
}

bool eliminar(QVector<Producto>& lista, const QString& codigo ){
    int pos = buscar(lista, codigo);
    if(pos==-1)
        return false;
    lista.remove(pos);
    guardar(lista);
    return true;
}
