#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QTableWidgetItem>
#include <QMessageBox>
#include <QAbstractItemView>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    ui->tableWidget->setEditTriggers(QAbstractItemView::NoEditTriggers);
    ui->tableWidget->setColumnWidth(0,60);
    ui->tableWidget->setColumnWidth(1,180);
    ui->tableWidget->setColumnWidth(2,100);
    ui->tableWidget->setColumnWidth(3,60);
    ui->tableWidget->setColumnWidth(4,60);
    ui->txtcodigo->clear();
    ui->txtnombre->clear();
    ui->txtprecio->clear();
    ui->txtanio->clear();
    ui->cmbtipo->setCurrentIndex(-1);
    ui->tableWidget->setColumnCount(5);
    QStringList encabezados;
    encabezados<<"codigo"<<"nombre"<<"tipo"<<"precio"<<"año";
    ui->tableWidget->setHorizontalHeaderLabels(encabezados);
    leer(lista);
    actualizartabla();
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::actualizartabla(){
    ui->tableWidget->setRowCount(lista.size());
    for(int i=0;i<lista.size();i++){
        ui->tableWidget->setItem(i,0,new QTableWidgetItem(lista[i].codigo));
        ui->tableWidget->setItem(i,1,new QTableWidgetItem(lista[i].nombre));
        ui->tableWidget->setItem(i,2,new QTableWidgetItem(lista[i].tipo));
        ui->tableWidget->setItem(i,3,new QTableWidgetItem(QString::number(lista[i].precio)));
        ui->tableWidget->setItem(i,4,new QTableWidgetItem(QString::number(lista[i].anio)));
    }
}
void MainWindow::on_btncrear_clicked()
{
    if(ui->txtcodigo->text().isEmpty() || ui->txtnombre->text().isEmpty() ||
        ui->txtprecio->text().isEmpty() || ui->txtanio->text().isEmpty() ||
        ui->cmbtipo->currentIndex() == -1){
        QMessageBox::warning(this, "Error", "Por favor complete todos los campos");
        return;
    }

    bool okPrecio, okAnio;
    double precio = ui->txtprecio->text().toDouble(&okPrecio);
    int anio = ui->txtanio->text().toInt(&okAnio);

    if(!okPrecio || precio <= 0){
        QMessageBox::warning(this, "Error", "El precio debe ser un número mayor a 0");
        return;
    }
    if(!okAnio || anio < 1800 || anio > 2026){
        QMessageBox::warning(this, "Error", "El año debe ser un número entre 1800 y 2026");
        return;
    }

    // Verificar codigo duplicado
    if(buscar(lista, ui->txtcodigo->text()) != -1){
        QMessageBox::warning(this, "Error", "Ya existe un producto con ese código");
        return;
    }

    Producto p;
    p.codigo = ui->txtcodigo->text();
    p.nombre = ui->txtnombre->text();
    p.tipo = ui->cmbtipo->currentText();
    p.precio = precio;
    p.anio = anio;
    crear(lista, p);
    actualizartabla();
    QMessageBox::information(this, "Correcto", "Producto agregado");
    ui->txtcodigo->clear();
    ui->txtnombre->clear();
    ui->txtprecio->clear();
    ui->txtanio->clear();
    ui->cmbtipo->setCurrentIndex(-1);
}


void MainWindow::on_btnmostrar_clicked()
{
    if(ui->txtcodigo->text().isEmpty()){
        QMessageBox::warning(this, "Error", "Ingrese un código para buscar");
        return;
    }

    QString codigo=ui->txtcodigo->text();
    leer(lista);
    ui->tableWidget->setRowCount(0);
    for(Producto& p: lista){
        if(p.codigo==codigo){
            int fila = ui->tableWidget->rowCount();
            ui->tableWidget->insertRow(fila);
            ui->tableWidget->setItem(fila,0,new QTableWidgetItem(p.codigo));
            ui->tableWidget->setItem(fila,1,new QTableWidgetItem(p.nombre));
            ui->tableWidget->setItem(fila,2,new QTableWidgetItem(p.tipo));
            ui->tableWidget->setItem(fila,3,new QTableWidgetItem(QString::number(p.precio)));
            ui->tableWidget->setItem(fila,4,new QTableWidgetItem(QString::number(p.anio)));
            ui->txtcodigo->setText(p.codigo);
            ui->txtnombre->setText(p.nombre);
            ui->cmbtipo->setCurrentText(p.tipo);
            ui->txtprecio->setText(QString::number(p.precio));
            ui->txtanio->setText(QString::number(p.anio));
            return;
        }
    }
    QMessageBox::warning(this,"buscar", "producto no encontrado");
}


void MainWindow::on_btnmodificar_clicked()
{
    if(ui->txtcodigo->text().isEmpty() || ui->txtnombre->text().isEmpty() ||
        ui->txtprecio->text().isEmpty() || ui->txtanio->text().isEmpty() ||
        ui->cmbtipo->currentIndex() == -1){
        QMessageBox::warning(this, "Error", "Por favor complete todos los campos");
        return;
    }

    bool okPrecio, okAnio;
    double precio = ui->txtprecio->text().toDouble(&okPrecio);
    int anio = ui->txtanio->text().toInt(&okAnio);

    if(!okPrecio || precio <= 0){
        QMessageBox::warning(this, "Error", "El precio debe ser un número mayor a 0");
        return;
    }
    if(!okAnio || anio < 1800 || anio > 2026){
        QMessageBox::warning(this, "Error", "El año debe ser un número entre 1800 y 2026");
        return;
    }

    QString codigo = ui->txtcodigo->text();
    Producto p;
    p.codigo = codigo;
    p.nombre = ui->txtnombre->text();
    p.tipo = ui->cmbtipo->currentText();
    p.precio = precio;
    p.anio = anio;
    leer(lista);
    if(modificar(lista, codigo, p)){
        leer(lista);
        actualizartabla();
        QMessageBox::information(this, "Modificar", "Producto actualizado");
    } else {
        QMessageBox::warning(this, "Modificar", "Código no encontrado");
    }
}



void MainWindow::on_btneliminar_clicked()
{
    if(ui->txtcodigo->text().isEmpty()){
        QMessageBox::warning(this, "Error", "Ingrese un código para eliminar");
        return;
    }

    QMessageBox::StandardButton confirmacion = QMessageBox::question(
        this, "Confirmar", "¿Está seguro que desea eliminar este producto?",
        QMessageBox::Yes | QMessageBox::No);

    if(confirmacion == QMessageBox::No) return;

    QString codigo = ui->txtcodigo->text();
    if(eliminar(lista, codigo)){
        leer(lista);
        actualizartabla();
        QMessageBox::information(this, "Eliminar", "Producto eliminado");
        ui->txtcodigo->clear();
        ui->txtnombre->clear();
        ui->txtprecio->clear();
        ui->txtanio->clear();
        ui->cmbtipo->setCurrentIndex(-1);
    } else {
        QMessageBox::warning(this, "Eliminar", "Código no encontrado");
    }
}

void MainWindow::on_btnrefrescar_clicked()
{
    leer(lista);
    actualizartabla();
}


void MainWindow::on_btndel_clicked()
{
    ui->txtcodigo->clear();
    ui->txtnombre->clear();
    ui->txtprecio->clear();
    ui->txtanio->clear();
    ui->cmbtipo->setCurrentIndex(-1);
}

