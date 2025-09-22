-- SQLite database schema for sales records
-- Table: ventas (sales)

CREATE TABLE IF NOT EXISTS ventas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha TEXT NOT NULL,
    tipo TEXT,
    punto_de_venta TEXT,
    numero_desde TEXT,
    numero_hasta TEXT,
    cod_autorizacion TEXT UNIQUE,
    tipo_doc_receptor TEXT,
    nro_doc_receptor TEXT,
    denominacion_receptor TEXT,
    tipo_cambio REAL,
    moneda TEXT,
    neto_grav_iva_0 REAL,
    iva_25 REAL,
    neto_grav_iva_25 REAL,
    iva_5 REAL,
    neto_grav_iva_5 REAL,
    iva_105 REAL,
    neto_grav_iva_105 REAL,
    iva_21 REAL,
    neto_grav_iva_21 REAL,
    iva_27 REAL,
    neto_grav_iva_27 REAL,
    neto_gravado_total REAL,
    neto_no_gravado REAL,
    op_exentas REAL,
    otros_tributos REAL,
    total_iva REAL,
    imp_total REAL,
    cuit TEXT,
    created_at TEXT
);

