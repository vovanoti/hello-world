Задача 1. Работа с локальным репозиторием

  1. Создать локальный репозиторий "git-lesson"
  [student@localhost git-lesson]$ git config --global user.name "vovanoti"
  [student@localhost git-lesson]$ git config --global user.email v_smirnovch@mail.ru
  
  [student@localhost git-lesson]$ git init
  Initialized empty Git repository in /home/student/chapter15/git-lesson/.git/
  
  2. Создать пустой файл README.md и закоммитить изменения.
  [student@localhost git-lesson]$ vi README.md
  [student@localhost git-lesson]$ git add .
  [student@localhost git-lesson]$ git commit -m "Add README.md"

  3. Создать дополнительную ветку "feat1-add-readme", добавить в файл README.md немного текста. Изменения закоммитить.
  [student@localhost git-lesson]$ git checkout -b feat1-add-readme
Switched to a new branch 'feat1-add-readme'
  [student@localhost git-lesson]$ vi README.md
  [student@localhost git-lesson]$ git add .
  [student@localhost git-lesson]$ git commit -m "Changed the branch"

  4. Переключиться обратно на "master" ветку и так же добавить в README.md немного другого текста
  [student@localhost git-lesson]$ git checkout master
Switched to branch 'master'
  [student@localhost git-lesson]$ vi README.md
  [student@localhost git-lesson]$ git add .
  [student@localhost git-lesson]$ git commit -m "Changed branch to the master"

  5. Смержить изменения из "feat1-add-readme" в "master" ветку так, чтобы сохранились изменения только из "feat1-add-readme" ветки
  [student@localhost git-lesson]$ git merge feat1-add-readme
  [student@localhost git-lesson]$ vi README.md
  [student@localhost git-lesson]$ git add .
  [student@localhost git-lesson]$ git commit -m "replaced README from the second branch"

  6. Переключиться обратно на "feat1-add-readme" ветку, создать файл temp_file и закоммитить изменения
  [student@localhost git-lesson]$ git checkout feat1-add-readme
  [student@localhost git-lesson]$ vi temp_file
  [student@localhost git-lesson]$ git add .
  [student@localhost git-lesson]$ git commit -m "create a temp file"

  7. Отменить изменения, вносимые первым коммитом ветки "feat1-add-readme"
  [student@localhost git-lesson]$ git log
  [student@localhost git-lesson]$ git revert db94e12a339459a7df5d8ba18175675ffcf3ead3
  [feat1-add-readme e3f6b6b] Revert "Changed the branch"
  1 file changed, 1 deletion(-)

Задача 2. Работа с удаленным репозиторием

  1. Создать пустой репозиторий в GitHub "git-lesson".
  https://github.com/vovanoti/git-lesson.git
  
  2. Сделать этот репозиторий удаленным для локального репозитория из первой задачи
  [student@localhost git-lesson]$ git remote add origin https://github.com/vovanoti/git-lesson.git
  
  
  3. Отправить изменения из всех веток в "git-lesson" репозиторий
  [student@localhost git-lesson]$ git checkout master
  [student@localhost git-lesson]$ git push -u origin master
  [student@localhost git-lesson]$ git checkout feat1-add-readme
  [student@localhost git-lesson]$ git push -u origin feat1-add-readme
  
  4. Заменить содержимое README.md в ветке "feat1-add-readme" строкой "Hello Github", закоммитить и отправить в "git-lesson" репо
  [student@localhost git-lesson]$ vi README.md
  [student@localhost git-lesson]$ git add .
  [student@localhost git-lesson]$ git commit -m "Changed readme for github"
  [student@localhost git-lesson]$ git push -u origin feat1-add-readme
  
  5. Сделать Pull-Request из ветки "feat1-add-readme" в "master" и добавить меня (@vauboy) ревьювером
  [student@localhost git-lesson]$ git checkout master
  [student@localhost git-lesson]$ git merge feat1-add-readme
  [student@localhost git-lesson]$ git add .
  [student@localhost git-lesson]$ git commit -m "Changed the master one last time"
  [student@localhost git-lesson]$ git fetch https://github.com/vovanoti/git-lesson.git
  [student@localhost git-lesson]$ git merge origin/master
  [student@localhost git-lesson]$ git push origin master
  
  Почему-то не может найти @vauboy в качестве reviewer'а

Задача 3. Знакомство с GitLab Community Edition

  1. Запустить Gitlab CE в докере "gitlab/gitlab-ce:latest"
  [student@localhost git-lesson]$ sudo docker pull gitlab/gitlab-ce:latest
