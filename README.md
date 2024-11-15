# Understanding hook in Helm!

Create a directory for helm hook:

```mkdir python-api-project/templates/hooks```

To install a pod that waits 10 seconds before to execute python-project. Edit the file pre-install.yml and change:

```---```
<br>```apiVersion: batch/v1```
<br>```kind: Job```
<br>```metadata:```
<br>```  name: "{{ include "python-api-project.fullname" . }}-pre-install-job-hook"```
<br>```  labels:```
<br>```    {{- include "python-api-project.labels" . | nindent 4 }}```
<br>```  annotations:```
<br>```    "helm.sh/hook": "pre-install"```
<br>```    "help.sh/hook-weith": "0"```
<br>```    "help.sh/hook-delete-policy": hook-succeded```
<br>```spec:```
<br>```  template:```
<br>```    spec:```
<br>```      containers:```
<br>```      - name: pre-install```
<br>```        image: busybox```
<br>```        imagePullPolicy: IfNotPresent```
<br>```        command: ['sh', '-c', 'echo pre-install Pod is Running ; sleep 10']```
<br>```      restartPolicy: OnFailure```
<br>```      terminationGracePeriodSeconds: 0```
<br>```  backoffLimit: 3```
<br>```  completions: 1```
<br>```  parallelism: 1```

Instala en Openshift la solucion Helm con el comando:

```helm install mypython python-api-project```

Before to install python project, Executes pod for wait 10 seconds:

fin
