<h1>GIT - Comandos, truquitos y más</h1>

**RECOMENDACIÓN: HACER UN CAMBIO POR COMMIT, NO MIL (COMO VENGO HACIENDO)**

<h2>Lista de comandos útiles:</h2>

 - `git init` -> Inicializa un repo de git en el cwd (current working directory, aka, donde estás parado!)

 - `git config --global user.name 'Gus'`

 - `git config --global user.email 'em@il.com'`

 - `git config --list` -> Ver la lista de configuraciones al git.

 - `git status` -> Ves en qué situación estás (si hay archivos modificados, si hay cosas que están listas para commitear, ---)

 - `git add -A` -> Para agregar archivos y carpetas que sufrieron cambios (creación, modificación o borrado) a la 'Staging Area' (paso previo al commit)

 - `git reset` -> Es para ir un paso hacia atrás (Staging Area -> Working Directory). Digamos que si hiciste 'add <file>' y no lo querías, con ese comando vas para atrás. Si no aclarás nada, resetea todo. Sino, es `git reset <file>`

 - `git commit -m 'Mensaje útil'` -> Es para pasar los archivos que estaban en la 'Staging Area' al '.git directory (Repositorio)'. Digamos que acá ya estarían en situación de ser subidos a internet.

 - `git log` -> Muestra un log donde queda asentados los commit que fuimos haciendo.

 - `git log --oneline` -> Versión más cómoda del log. Te muestra HASH y comentario, re piola.

Hasta acá estamos trackeando nuestro proyecto local.

Ahora, queremos trackear un proyecto remoto, cómo hacemos?

 - `git clone <url> <where to clone>` -> Descarga un repositorio git en la dirección especificada. Ahora tenés una versión local del repo!

 - `git remote -v` -> Te muestra la URL del repo que tenés.

 - `git branch -a` -> Muestra los branches del repo (local y remotos)

 - `git diff` -> Te muestra qué cambió en los archivos.

 - `git pull` -> Te baja todo lo que se fue modificando en el repo remoto a la compu.

 - `git push origin master` -> Para subir del repo local al repo remoto. 'origin' es el nombre del repo remoto y 'master' es el branch al que lo estamos subiendo.
 
Más comandos copados:

- **Alias**. Se puede ahorrar un poco de tipeo tipo `git log --oneline --all --graph` y escribir algo tipo `git lodag` como un alias para el comando. Para esto:
   - `git config --global alias.nombreQueQueremos 'comando posta'`
   - Cómo listar todos los alias? `git config --global --get-regexp alias`
   - Para eliminar un alias: `git config --global --unset alias.algo`


<h2>Para ignorar archivos en el directorio</h2>
Lo que hay que hacer es armar un .gitignore

`touch .gitignore`

Dentro de ese archivo ponés lo que no querés que se suba!

<h2> Workflow más común usando git </h2>

 - Crear un branch para el feature a desarrollar:

    - `git branch nombre-del-feature` -> Lo crea

    - `git branch` -> Lista los branches existentes. El que tiene asterisco es en el que se está trabajando actualmente.

 - Cambiar al branch creado:

    - `git checkout nombre-de-feature` -> Cambia a ese branch.

 - Luego, laburás tranqui en el archivo, hacés todos los cambios que tengas ganas.

 - Subís eso a tu local repo:

    - `git add -A`

    - `git commit -m 'mensaje'`

    - `git commit --ammend` -> Uh, me olvidé de subir un cambio de último momento. será que puedo meter ese cambio en el último commit sin tener que crear otro? Ahí se usa ese código. Primero mandás el `git add <file>` que te faltaba y luego el comando dicho.

 - Subís los cambios al repo remoto:

    - `git push -u origin nombre-de-feature` -> Esto pushea al branch remoto (me imagino que si nunca lo habías hecho antes, primero lo crea). El -u lo que hace es asociar ambos branches para que, en el futuro, solo tenga que hacer `git push` o `git pull` (es piola eso).
    
    - `git branch -a` -> Vemos los branches (locales y remotos). Ahora podemos ver que existe un branch en el repo remoto llamado nombre-del-feature.
    
 - Cuando está todo re testeado y seguro que funciona bien, vas a querer 'mergear' el branch con 'master.

   - `git checkout master` -> Cambiamos al branch master.

   - `git pull origin master` -> Pulleamos todos los cambios antes de commitear o pushear (pensando en que pudieron haber cambios que subieron otros en el medio).

   - `git branch --merged` -> Muestra los branches que fueron mergeados hasta el momento.

   - `git merge nombre-de-feature` -> Mergeas el branch  nombre-de-feature con el branch en el que estás parado (en este caso, master).

   - `git push origin master` -> Pusheas al master (queda todo unificado).

 - Ahora, el branch ya no tiene uso, hay que borrarlo:

   - `git branch --merged` -> Para doble chequear que todo se mergeó bien.

   - `git branch -d nombre-de-feature` -> Borramos el branch en cuestión (local).

   - `git branch -a`-> Podemos ver con este comando para ver que se borró, pero aún lo vemos en el repo remoto.

   - `git push origin --delete nombre-de-feature` -> Borramos el branch en el repo remoto.

<h2>Cómo revertir cambios con Git</h2>

Se supone que estas es una de las utilidades más piolas del git. Digamos que venimos trabajando en nuestro archivo, y tenemos un par de commits hechos.
Meto un cambio en el archivo, y me doy cuenta que la cagué y que mi ctrl-z me falló. Pero yo hace poquito lo había mandado a la 'Staging Area' (NO COMMIT).

Planteamos 3 instancias:

1. Tenía mi archivo ya subido (`add <file>`), lo modifiqué localmente y quiero revertir.

 - Uso `git diff` para poder ver la versión anterior subida a la Staging Area. Ahí puedo ver la lista de diferencias respecto de ambos archivos.

 - Para deshacer el cambio, `git checkout -- <file>`. Listo, ya recuperé mis cambios.

 - Digamos que me recupera hasta el último 'add'.

2. Modifiqué mi archivo. Lo subí (`git add <file>`). Ahora hice otra modificación. Ahora lo que quiero modificar es la versión Stageada (no la local).

 - `git reset HEAD <file>` -> Esto lo que hace es bajar de Stage a Working el último add hecho en el branch en el que estoy parado.

 - Ahora sí puedo `git checkout -- <file>` y revierto los cambios.

3. Hice `git commit`. Quiero bajarlo para modificar o lo que sea.

 - `git log --oneline` -> Primero conviene pasar por acá para ver la lista de commits. En particular, el último que queremos deshacer. Copiamos el hash.

 - `git reset <hash>` -> Lo vuela. Ahora, si hacemos `git status` vemos que el cambio anterior vuelve a estar en 'Staging Area' en rojo, como antes de hacer `add`.

 - Solo queda `git checkout <file>` para revertir esos cambios.

 - Se puede hacer en un solo paso con `git reset --hard <hash>`. Deshace el commit vuelve a estar parado en el anterior) y hace un checkout (elimina los cambios realizados).

 - Si, por el contrario, queremos que resetee pero las cosas que hice `add` no las quite, hacemos `git reset --soft <hash>`.

<h2>Comando revert</h2>
 
Ahora vamos a ver otra situación con el comando `revert`. Es un mejor comando para deshacer cambios. `reset` es complicado en varias situaciones; una, por ejemplo, es si varias personas tienen acceso al repo. Se generarían conflictos difíciles de arreglar si eliminás un commit.

Situación:
   Le damos nuestra web al diseñador gráfico y cuando la volvemos a agarrar está horrible xd. El flaco hizo cambios y los mandó todos a un commit. Qué hacemos? Conviene user `revert` en lugar de `reset` para que no haya lío con las versiones que tenemos ambos.
1. Primero, podemos ver qué cambios hubo. Tenemos dos formas de hacerlo (da igual cualquiera de ellas):
   - `git diff <hash_1> <hash_2>` -> Compara dos commits cualesquiera
   - `git diff HEAD~1` -> Compara la situación actual (HEAD) con n commits anterior.
2. Luego:
   - `git revert HEAD` (o, lo mismo, el hash del último commit)
   Esto revierte los cambios que fueron modificados de un commit a otro.

<h2>Branching - Qué es y para qué sirve</h2>

La idea de ramificar el trabajo es tener un código central siempre limpio y funcional, a la vez que, en paralelo (en un branch) vamos creando nuevas funcionalidades y solucionando problemas. Una vez que esto está terminado, se procede al *merge*.

Tenemos como ventaja que podemos hacer varias cosas a la vez (multitasking). Tenés un programa principal y estás trabajando en algo en particular (para lo cual armaste una rama). Te llaman y te dicen que tenés que hacer una serie de cambios INMEDIATAMENTE. Ahí lo más conveniente es dejar la rama en la que estábamos trabajando, armar una rama para el problema, solucionarlo, mergear, y seguir con tu vida.

Un poco de esto ya lo tenemos más arriba en el Workflow. Vamos a agregar algunas cositas.

- Crear una rama y cambiarme a ella de una: `git branch -b nombre-de-rama`
- Renombrar una rama: `git branch -m nombre-de-rama nombre-nuevo-de-rama`
- Borrar rama (está más arriba): `git branch -d nombre-de-rama`

Cuestión. Armamos el branch, hacés modificaciones ahí. Trabajás de la misma forma, `git add`, `git commit -m 'msg'`.
Si queremos volver a hacer algo en la principal, `git checkout master` y le damos ahí, o hacemos otro branch. Las cosas en branches separados tienen sus propios archivos. Si cambiamos entre branches podemos ver, efectivamente, como el código de uno modificado no aparece en el otro.

<h2>Merge</h2>

Cuando ya está todo esto, vamos a querer proceder a **mergear**.
1. Nos vamos al branch que queremos que reciba los cambios (rama de destino): `git checkout master`
2. Mergeamos el branch. `git merge nombre-de-rama`

Puede hacer el merge con fast-forward (cuando fusionamos una rama con modificaciones y una sin modificaciones) o mediante una estrategia recursiva (cuando ambas tienen modificaciones).

Puede pasar que la fusión no sea tan sencilla y ocurran **conflictos**!

Cuando procedés al merge te avisa que hay un conflicto (algo que no pudo solucionar mediante recursión). Acá vas al archivo en cuestión y ves algo tipo:

`<<<<<<HEAD
UNA VERSION DEL TEXTO
===================
>>>>>> nombre-de-branch`

Lo que hay que hacer es, manualmente, borrar y quedarse con lo mejor de ambos (o lo que quieras), borrando todos los simbolitos y demás.
Luego normal, `git add` `git commit` y ya.

Si la cagaste y no querés que se metan los cambios del merge, `git merge --abort`

<h2>Tags</h2>

Los tags son una forma de alias para versiones específicas que nos interesen. Por ejemplo, si tenemos un programa con un commit que correspondería con su versión v0.1.0, la podemos taggear para poder ir a ella más fácilmente que usando el hash.
 - `git tag v0.1.0` -> Tagea el commit en el que estamos parados
 - `git tag v0.1.0 <hash>` -> Tagea ese hash en particular
 - `git tag` -> Lista los distintos tags existentes.
 - `git tag -d 'v0.1.0` -> Borra el tag.

<h2>Stash</h2>

Qué pasa cuando estamos trabajando en un branch y queremos cambiar a otro **pero teníamos cosas en la Staging Area (ya habíamos hecho** `git add <file>`**)?.** Una opción es hacer el `commit`, pero quizás aún no queríamos. Existe el comando `stash`:

- `git stash` -> Guarda todo lo que está en la Staging Area a un temporal.

- Podemos ponerle un nombre para que sea más descriptivo: `git stash save 'mensaje'`

Podemos ir apilando varios *stash*, que van quedando en modo de pila.

La idea es que ahí podemos cambiar tranquilamente de branches, hacer lo que queramos. Luego, volvemos a nuestro branch. Y ahí recuperamos:

- `git stash apply` -> Lo último stasheado vuelve a la Staging Area! La info de todas formas sigue guardado en el stash, por cualquier cosa.

Con el comando `git stash apply` se van aplicando en el orden en el que están (como una pila).

Si lo que se quiere es aplicarlo al Staging Area **Y** borrarlo, entonces:

- `git stash pop` -> Aplica lo del stash al Staging y lo borra.

Podemos usar el comando `git stash list` para ver las cosas que mandamos al Stash.

Finalmente, para borrar el stash: `git stash drop`. Esto borra el último. Si lo que queremos es borrar todo:

- `git stash clear` o:

- `git stash <id>` -> Borra uno específico

Podés aplicar stashes específicos también. Si tenés varios tipo:
- stash@{0}
- stash@{1}
- stash@{2}
- stash@{3}
Podés hacer:
- `git stash apply stash@{1}`
- `git stash apply stash@{2}`
