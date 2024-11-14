# Let's move Docker to Openshift Python Quote Bot!

Create a helm solution with following command:

```helm create python-api-project```

Edit the file values.yaml and change:

>(Line 10)   repository: nginx   --->   juancvilla/python-api-project:python-project
>
>(Line 55)   type: ClusterIP   --->   type: NodePort

Edit the file Chart.yaml and change:

>(Line 24)   appVersion: "1.16.0"   --->   # appVersion: "1.16.0"

Edit the file template/deployment.yaml

>   image: "{{ .Values.image.repository }}:{{ .Values.image.tag | default .Chart.AppVersion }}"
>
>   --->
>
>   image: "{{ .Values.image.repository }}"
>
>   containerPort: {{ .Values.service.port }}   --->   containerPort: 9001
>
>(delete line) livenessProbe:
> 
>(delete line)   {{- toYaml .Values.livenessProbe | nindent 12 }}
>
>(delete line) readinessProbe:
>
>(delete line)   {{- toYaml .Values.readinessProbe | nindent 12 }}

Instala en Openshift la solucion Helm con el comando:

```helm install mypython python-api-project```

```oc get svc```

```oc expose svc mypython-python-api-project```

```oc get route```

```curl http://mypython-python-api-project-jvillarroelquintec-dev.apps.sandbox-m3.1530.p1.openshiftapps.com/quote```

fin
