#ifndef MAINWINDOW_H
#define MAINWINDOW_H


#include <QMainWindow>
#include <QVector>
#include"productos.h"
#include "funciones.h"

QT_BEGIN_NAMESPACE
namespace Ui {
class MainWindow;
}
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT


public:
    explicit MainWindow(QWidget *parent = nullptr);
    ~MainWindow() override;
private slots:
    void on_btncrear_clicked();
    void on_btnmostrar_clicked();
    void on_btnmodificar_clicked();
    void on_btneliminar_clicked();

    void on_btnrefrescar_clicked();

    void on_btndel_clicked();

private:
    Ui::MainWindow *ui;
    QVector<Producto> lista;
    void actualizartabla();
};
#endif // MAINWINDOW_H
