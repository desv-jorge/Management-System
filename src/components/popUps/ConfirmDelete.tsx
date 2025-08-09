interface PopupConfirmProps {
  message: string;
  onConfirm: () => void;
  onCancel: () => void;
}

export default function PopupConfirm({ message, onConfirm, onCancel }: PopupConfirmProps) {
  return (
    <div
      className="fixed inset-0 flex justify-center items-center z-50"
      style={{
        backgroundColor: "rgba(0, 0, 0, 0.3)",
        backdropFilter: "blur(5px)",
        WebkitBackdropFilter: "blur(5px)",
      }}
    >
      <div className="bg-white rounded-lg p-6 max-w-sm w-full shadow-lg">
        <p className="mb-6 text-gray-800">{message}</p>
        <div className="flex justify-end gap-4">
          <button
            onClick={onCancel}
            className="px-4 py-2 rounded border border-gray-400 hover:bg-gray-100 cursor-pointer"
          >
            Não
          </button>
          <button
            onClick={onConfirm}
            className="px-4 py-2 rounded bg-red-600 text-white hover:bg-red-700 cursor-pointer"
          >
            Sim
          </button>
        </div>
      </div>
    </div>
  );
}

