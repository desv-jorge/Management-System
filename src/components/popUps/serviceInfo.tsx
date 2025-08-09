interface PopupServiceInfoProps {
  service: any;
  onClose: () => void;
}

export default function PopupServiceInfo({ service, onClose }: PopupServiceInfoProps) {
  return (
    <div className="fixed inset-0 bg-black/50 backdrop-blur-sm flex items-center justify-center px-4">
      <div className="bg-white rounded-xl shadow-lg p-6 max-w-lg w-full relative">
        <button
          onClick={onClose}
          className="absolute top-3 right-3 text-gray-600 hover:text-black text-xl cursor-pointer"
        >
          ✕
        </button>

        <h2 className="text-2xl font-bold mb-4">Informações do Serviço</h2>

        <p><strong>Cliente:</strong> {service.client}</p>
        <p><strong>Aparelho:</strong> {service.device}</p>
        <p><strong>Momento da solicitação:</strong> {service.created_at}</p>
        <p className="mt-2"><strong>Email:</strong> {service.email}</p>

        <div className="mt-4">
          <strong>Descrição:</strong>
          <p className="bg-gray-100 p-2 rounded mt-1">{service.description}</p>
        </div>
      </div>
    </div>
  );
}
