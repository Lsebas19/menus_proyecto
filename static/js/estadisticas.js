// ====== REFERENCIAS A ELEMENTOS DEL DOM ======
        const barraLateral = document.getElementById('barraLateral');
        const contenidoPrincipal = document.getElementById('contenidoPrincipal');

        // ====== FUNCIONALIDAD: ABRIR BARRA LATERAL CON HOVER EN BORDE IZQUIERDO ======
        // Zona de activación: borde izquierdo de 10px
        const zonaActivacion = document.createElement('div');
        zonaActivacion.style.cssText = `
            position: fixed;
            left: 0;
            top: var(--header-height);
            bottom: 0;
            width: 15px;
            z-index: 45;
        `;

        zonaActivacion.addEventListener('mouseenter', () => {
            barraLateral.classList.remove('contraida');
        });

        document.body.appendChild(zonaActivacion);

        barraLateral.addEventListener('mouseenter', () => {
            barraLateral.classList.remove('contraida');
        });

        barraLateral.addEventListener('mouseleave', () => {
            barraLateral.classList.add('contraida');
        });

        contenidoPrincipal.addEventListener('mouseenter', () => {
            barraLateral.classList.add('contraida');
        });

        // ====== FUNCIONALIDAD: ALTERNAR PANELES CON ANIMACIÓN ======
        function alternarPanel(btn) {
            const panel = btn.closest('.panel');
            const contenido = panel.querySelector('.contenido-panel');
            
            // Alternar clases
            btn.classList.toggle('abierto');
            contenido.classList.toggle('abierto');
            
            // Animación suave: desplazar si se abre
            if (contenido.classList.contains('abierto')) {
                contenido.style.animation = 'none';
                setTimeout(() => {
                    contenido.style.animation = 'deslizarAbierto 0.4s ease-out forwards';
                }, 10);
            }
        }

        // ====== FUNCIONALIDAD: MARCAR ELEMENTO ACTIVO EN BARRA LATERAL ======
        document.querySelectorAll('.elemento-barra').forEach(item => {
            if (item.href.includes(window.location.pathname)) {
                item.classList.add('activo');
            }
        });