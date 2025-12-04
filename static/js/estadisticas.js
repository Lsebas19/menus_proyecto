// ====== REFERENCIAS A ELEMENTOS DEL DOM ======
        const contenidoPrincipal = document.getElementById('contenidoPrincipal');



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

        