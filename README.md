# Understanding hook in Helm!

Create a directory for helm hook:

```bash
mkdir python-api-project/templates/hooks
```

To install a pod that waits 10 seconds before to execute python-project. Edit the file pre-install.yml and change:

```bash
---
apiVersion: batch/v1

kind: Job
metadata:
  name: "{{ include "python-api-project.fullname" . }}-pre-install-job-hook"
  labels:
    {{- include "python-api-project.labels" . | nindent 4 }}
  annotations:
    "helm.sh/hook": "pre-install"
    "help.sh/hook-weith": "0"
    "help.sh/hook-delete-policy": hook-succeded
spec:
  template:
    spec:
      containers:
      - name: pre-install
        image: busybox
        imagePullPolicy: IfNotPresent
        command: ['sh', '-c', 'echo pre-install Pod is Running ; sleep 10']
      restartPolicy: OnFailure
      terminationGracePeriodSeconds: 0
  backoffLimit: 3
  completions: 1
  parallelism: 1
```


Instala en Openshift la solucion Helm con el comando:

```helm install mypython python-api-project```

Before to install python project, Executes pod for wait 10 seconds:

fin
