from client import NoCodeSpatialXr3dSceneSimulatorClient

def main():
    client = NoCodeSpatialXr3dSceneSimulatorClient()
    desc = "Interactive futuristic control room with floating holographic telemetry panels"
    res = client.generate_xr_scene(desc)
    print(f"Physics Enabled: {res['physics_enabled']}")
    print(f"Entities Count: {res['interactive_entities_count']}")
    print("Scene Schema:", res["scene_schema_json"])

if __name__ == "__main__":
    main()
