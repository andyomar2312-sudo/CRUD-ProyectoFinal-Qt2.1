#ifndef FUNCIONES_H
#define FUNCIONES_H
#include <QString>
#include <QVector>
#include "productos.h"
extern QString ruta;

void guardar(const QVector<Producto>& lista);
void leer(QVector<Producto>& lista);
void crear(QVector<Producto>& lista, const Producto& nuevo);
bool modificar(QVector<Producto>& lista, const QString& codigo, const Producto& nuevo);
bool eliminar(QVector<Producto>& lista, const QString& codigo );
int buscar (QVector<Producto>& lista, const QString& codigo);

#endif // FUNCIONES_H
