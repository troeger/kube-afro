from rest_framework import serializers, generics

from kubeportal.models.kubernetesserviceaccount import KubernetesServiceAccount


class ServiceAccountSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    namespace = serializers.HyperlinkedRelatedField(view_name='namespace', lookup_field='name', lookup_url_kwarg='name', read_only=True)


    class Meta:
        model = KubernetesServiceAccount
        fields = ['name', 'namespace']


class ServiceAccountView(generics.RetrieveAPIView):
    lookup_field = 'uid'
    serializer_class = ServiceAccountSerializer

    def get_queryset(self):
        # Clients can only request details of the service accounts that are assigned to them
        return self.request.user.k8s_accounts()
