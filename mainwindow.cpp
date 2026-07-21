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
    Producto p;
    p.codigo=ui->txtcodigo->text();
    p.nombre=ui->txtnombre->text();
    p.tipo=ui->cmbtipo->currentText();
    p.precio=ui->txtprecio->text().toDouble();
    p.anio=ui->txtanio->text().toInt();
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
    QString codigo= ui->txtcodigo->text();
    Producto p;
    p.codigo=ui->txtcodigo->text();
    p.nombre=ui->txtnombre->text();
    p.tipo=ui->cmbtipo->currentText();
    p.precio=ui->txtprecio->text().toDouble();
    p.anio=ui->txtanio->text().toInt();
    leer(lista);
    if(modificar(lista, codigo,p)){
        leer(lista);
        actualizartabla();
        QMessageBox::information(this, "modificar","producto actualizado");
    }else{
        QMessageBox::warning(this,"modificar","codigo no encontrado");
    }

}




void MainWindow::on_btneliminar_clicked()
{
    QString codigo= ui->txtcodigo->text();

    if(eliminar(lista, codigo))
    {
        leer(lista);
        actualizartabla();
        QMessageBox::information(this ,"eliminar","producto eliminado");
        ui->txtcodigo->clear();
        ui->txtnombre->clear();
        ui->txtprecio->clear();
        ui->txtanio->clear();
        ui->cmbtipo->setCurrentIndex(-1);
    }
    else{
        QMessageBox::warning(this ,"eliminar","codigo no encontrado");
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

